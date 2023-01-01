import os
import argparse
import time
from core.database.engine import save
from core.database.schema import Result
from core.large_language_models.codex import apply_response_to_fixed_version, fix_bug_by_openai_codex, revert_response_to_fixed_version

from core.utils import get_benchmark

parser = argparse.ArgumentParser(
    prog="fixa", description='Checkout and fix the bug by pre-trained large language model')
parser.add_argument("--model", "-m", required=True,
                    help="The pre-trained large language model (for example, codex)")
parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                    help="The benchmark to repair")
parser.add_argument("--project", "-p", required=False,
                    help="The project name (case sensitive)")
parser.add_argument("--id", "-i", required=False, help="The bug id")
parser.add_argument("--working_directory", "-w",
                    required=True, help="The working directory")
parser.add_argument("--type", "-t",
                    required=False, help="type: dryrun")

DEFECTS4J_BUG_SIZE = {
    'Chart': 26,
    'Cli': 40,
    'Closure': 176,
    'Codec': 18,
    'Collections': 28,
    'Compress': 47,
    'Csv': 16,
    'Gson': 18,
    'JacksonCore': 26,
    'JacksonDatabind': 112,
    'JacksonXml': 6,
    'Jsoup': 93,
    'JxPath': 22,
    'Lang': 65,
    'Math': 106,
    'Mockito': 38,
    'Time': 27,
}


def checkout_bug(benchmark, project, bug_id, version):
    bug_identifier = args.project + '_' + bug_id

    bug_path = os.path.join(args.working_directory,
                            "%s_%s_%s_%s" % (benchmark.name, project, bug_id, version))

    print('bug_identifier: ', bug_identifier)
    bug = benchmark.get_bug(bug_identifier)
    print('bug: ', bug)
    is_buggy_version = version == 'buggy'
    bug.checkout(bug_path, is_buggy_version)

    return bug


def fix_single_bug(args, bug_id, fixa_config):
    result = Result()
    result.buggy_code_chunk = ''
    result.model = args.model
    result.benchmark = args.benchmark
    result.project = args.project
    result.bug_id = bug_id
    result.request_type = 'SINGLE_FUNCTION'

    benchmark = get_benchmark(args.benchmark)

    bug_dir = os.path.join(args.working_directory,
                           "%s_%s_%s" % (args.benchmark, args.project, bug_id))

    try:
        fixed_bug = checkout_bug(benchmark, args.project, bug_id, 'fixed')
    except Exception as e:
        print('-------bug {} {} does not exist or deprecated-------\n'.format(args.project, bug_id), e)
        return

    if fixa_config['compile']:
        fixed_bug.compile()
    if fixa_config['test']:
        fixed_bug.run_test()

    buggy_bug = checkout_bug(benchmark, args.project, bug_id, 'buggy')
    if fixa_config['compile']:
        buggy_bug.compile()
    if fixa_config['test']:
        buggy_bug.run_test()

    # Only support Codex with Defects4J for now
    if args.model == 'Codex' and args.benchmark == 'Defects4J':
        patch_file_path = 'benchmarks/defects4j/framework/projects/{}/patches/{}.src.patch'.format(
            args.project, bug_id)
        try:
            applied, result, original_buy_lines = fix_bug_by_openai_codex(result, args.working_directory, fixed_bug, patch_file_path,
                                                                          fixa_config['include_document'], fixa_config['include_comments'], fixa_config['dry_run'])
            if applied:
                print('bug from codex response has been applied')
                # compile the fixed version with the response from Codex
                compiled_output = fixed_bug.compile()
                result.respond_compiled_output = compiled_output
                if compiled_output.count('OK') == 2:
                    result.result_type = 'COMPILED_SUCCESS'
                test_output = fixed_bug.run_test()
                if test_output == True:
                    result.request_type = 'TEST_SUCCESS'
                else:
                    result.result_type = 'TEST_FAILED'
                # revert the codex response version to the original fixed version
                revert_response_to_fixed_version(
                    original_buy_lines, args.working_directory, fixed_bug, patch_file_path)
            save(result)
        except Exception as e:
            result.result_type = 'ERROR'
            result.error_message = str(e)
            save(result)
            print(
                '-------something wrong with bug {} {}-------'.format(args.project, bug_id), e)
    else:
        print('Only support Codex with Defects4J for now')
        exit(1)


fixa_config = {
    'include_document': False,
    'include_comments': True,
    'compile': True,
    'test': True,
    'dry_run': False,
    'sample': 200,
}

DEFECTS4J_PROJECTS = ['Chart', 'Cli', 'Closure', 'Codec', 'Collections', 'Compress', 'Csv', 'Gson',
                      'JacksonCore', 'JacksonDatabind', 'JacksonXml', 'Jsoup', 'JxPath', 'Lang', 'Math', 'Mockito', 'Time']


if __name__ == "__main__":
    args = parser.parse_args()
    dry_run = args.type == 'dryrun'

    if args.project != None and args.id == None:
        # fix all bugs from a project
        bug_size = DEFECTS4J_BUG_SIZE[args.project]
        for bug_id in range(1, bug_size + 1):
            fix_single_bug(args, str(bug_id), fixa_config)
            time.sleep(30)
    elif args.project == None and args.id == None:
        # fix all bugs from all projects
        for project, bug_size in DEFECTS4J_BUG_SIZE.items():
            args.project = project
            for bug_id in range(1, bug_size + 1):
                fix_single_bug(args, str(bug_id), fixa_config)
                time.sleep(30)
    else:
        fix_single_bug(args, args.id, fixa_config)
