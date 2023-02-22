import argparse
import os
import shutil
from dotenv import dotenv_values
from core.large_language_models.ask_codex_bugs_jar import get_bugs_config
from core.tools.log import printlog

from core.utils import get_benchmark

config = dotenv_values(".env")

parser = argparse.ArgumentParser(
    prog="ask", description='Checkout and fix the bug by pre-trained large language model')
parser.add_argument("--model", "-m", required=True,
                    help="The pre-trained large language model (for example, codex)")
parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                    help="The benchmark to repair")
parser.add_argument("--project", "-p", required=False,
                    help="The project name (case sensitive)")
parser.add_argument("--id", "-i", required=False, help="The bug id")
parser.add_argument("--start", "-s", required=False,
                    help="The bug id starts from")
parser.add_argument("--working_directory", "-w",
                    required=True, help="The working directory")


FIXA_CONFIG = {
    'include_document': False,
    'include_comments': True,
    'compile': True,
    'sample': int(config.get('CODEX_SAMPLE_SIZE') or 1),
    'completion_ratio': 1.2,
}

BUGS_DOT_JAR_PROJECTS = [
    'accumulo', 'camel', 'commons-math', 'flink', 'jackrabbit-oak', 'logging-log4j2', 'maven', 'wicket'
]


BUGS_DOT_JAR_BUG_SIZE = {
    'accumulo': 98,
    'camel': 147,
    'commons-math': 147,
    'flink': 70,
    'jackrabbit-oak': 278,
    'logging-log4j2': 81,
    'maven': 48,
    'wicket': 289,
}


def handle_buggy_version(args, benchmark):
    bug_data = get_bugs_config(args.project, args.id)
    bug = benchmark.get_bug('{}_{}'.format(args.project, args.id))

    # Checkout the buggy version
    buggy_bug_path = os.path.join(args.working_directory,
                                  "%s_%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id, 'buggy'))
    print('buggy_bug_path', buggy_bug_path)
    if os.path.exists(buggy_bug_path):
        print('will clean folder', buggy_bug_path)
        shutil.rmtree(buggy_bug_path)
    # True for buggy version, False for fixed version
    bug.checkout(buggy_bug_path, True)
    printlog('--compile--')
    compile_result = bug.compile()
    printlog('--compile result--', compile_result)
    compile_success = not 'BUILD FAILURE' in compile_result
    test_success = False
    if compile_success:
        print('buggy version compile passed')
        printlog('--run test on the buggy version--')
        test_result = bug.run_test()
        printlog('--test result of the buggy version--', test_result)
        if test_result['errors'] > 0 or test_result['failures'] > 0:
            print('test failed')
            test_success = False
        else:
            print('test passed')
            test_success = True
    else:
        print('buggy version compile failed')
    printlog('--end---')
    return compile_success, test_success


def handle_fixed_version(args, benchmark):
    bug_data = get_bugs_config(args.project, args.id)
    bug = benchmark.get_bug('{}_{}'.format(args.project, args.id))

    # Checkout the fixed version
    fixed_bug_path = os.path.join(args.working_directory,
                                  "%s_%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id, 'fixed'))
    print('fixed_bug_path', fixed_bug_path)
    if os.path.exists(fixed_bug_path):
        print('will clean folder', fixed_bug_path)
        shutil.rmtree(fixed_bug_path)
    # True for buggy version, False for fixed version
    bug.checkout(fixed_bug_path, False)
    printlog('--compile--')
    compile_result = bug.compile()
    printlog('--compile result--', compile_result)
    compile_success = not 'BUILD FAILURE' in compile_result
    test_success = False
    if compile_success:
        print('fixed version compile passed')
        printlog('--run test on the fixed version--')
        test_result = bug.run_test()
        printlog('--test result of the fixed version--', test_result)
        if test_result['errors'] > 0 or test_result['failures'] > 0:
            print('test failed')
            test_success = False
        else:
            print('test passed')
            test_success = True
    else:
        print('fixed version compile failed')
    printlog('--end---')
    return compile_success, test_success


if __name__ == "__main__":
    args = parser.parse_args()
    benchmark = get_benchmark(args.benchmark)

    buggy_compile_success, buggy_test_success = handle_buggy_version(
        args, benchmark)
    fixed_compile_success, fixed_test_success = handle_fixed_version(
        args, benchmark)

    print('------------------result for bug {}_{}------------------'.format(args.project, args.id))
    print('buggy_compile_success: ', buggy_compile_success)
    print('buggy_test_success: ', buggy_test_success)
    print('fixed_compile_success: ', fixed_compile_success)
    print('fixed_test_success: ', fixed_test_success)
