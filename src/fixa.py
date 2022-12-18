import os
import argparse
from core.large_language_models.codex import fix_bug_by_openai_codex

from core.utils import get_benchmark

parser = argparse.ArgumentParser(
    prog="fixa", description='Checkout and fix the bug by pre-trained large language model')
parser.add_argument("--model", "-m", required=True,
                    help="The pre-trained large language model (for example, codex)")
parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                    help="The benchmark to repair")
parser.add_argument("--project", "-p", required=True,
                    help="The project name (case sensitive)")
parser.add_argument("--id", "-i", required=False, help="The bug id")
parser.add_argument("--working_directory", "-w",
                    required=True, help="The working directory")
parser.add_argument("--type", "-t",
                    required=False, help="type: dryrun")

DEFECTS4J_BUG_SIZE = {
    'Chart': 26,
    'Closure': 176,
    'Lang': 65,
    'Math': 106,
    'Mockito': 38,
    'Time': 27
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


def fix_single_bug(args, bug_id, compile=True, test=True, dry_run=False):
    benchmark = get_benchmark(args.benchmark)

    bug_dir = os.path.join(args.working_directory,
                           "%s_%s_%s" % (args.benchmark, args.project, bug_id))

    fixed_bug = checkout_bug(benchmark, args.project, bug_id, 'fixed')
    if compile:
        fixed_bug.compile()
    if test:
        fixed_bug.run_test()

    buggy_bug = checkout_bug(benchmark, args.project, bug_id, 'buggy')
    if compile:
        buggy_bug.compile()
    if test:
        buggy_bug.run_test()

    # Only support Codex with Defects4J for now
    if args.model == 'Codex' and args.benchmark == 'Defects4J':
        patch_file_path = 'benchmarks/defects4j/framework/projects/{}/patches/{}.src.patch'.format(
            args.project, bug_id)
        try:
            response = fix_bug_by_openai_codex(
                bug_dir, patch_file_path, dry_run)
        except Exception as e:
            print(
                '-------something wrong with bug {} {}-------'.format(args.project, bug_id), e)
    else:
        print('Only support Codex with Defects4J for now')
        exit(1)


if __name__ == "__main__":
    args = parser.parse_args()
    dry_run = args.type == 'dryrun'

    if args.id == None:
        bug_size = DEFECTS4J_BUG_SIZE[args.project]
        for bug_id in range(1, bug_size + 1):
            fix_single_bug(args, str(bug_id), True, True, dry_run)
    else:
        fix_single_bug(args, args.id, True, True, dry_run)
