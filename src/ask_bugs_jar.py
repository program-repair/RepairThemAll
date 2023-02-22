import argparse
import os
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
parser.add_argument("--version", "-v",
                    required=True, help="buggy or fixed")


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


if __name__ == "__main__":
    args = parser.parse_args()
    benchmark = get_benchmark(args.benchmark)
    printlog('--benchmark--', benchmark)
    # bug = benchmark.get_bug(args.id)
    if args.version == "fixed":
        buggy_version = False
        version_str = "fixed"
    else:
        buggy_version = True
        version_str = "buggy"

    for project in BUGS_DOT_JAR_PROJECTS:
        get_bugs_config(project)

    # bug_path = os.path.join(args.working_directory,
    #                         "%s_%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id, version_str))
    # bug.checkout(bug_path, buggy_version)  # buggy or fixed
    # printlog('--bug--')
    # printlog(bug)
    # printlog(bug_path)
    # printlog('--compile--')
    # compile_result = bug.compile()
    # printlog('--compile result--', compile_result)
    # printlog('--run test--')
    # test_result = bug.run_test()
    # printlog('--test result--', test_result)
    # printlog('--end---')
