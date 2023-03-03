import argparse
import os
import time
from core.large_language_models.ask_codex_defects4j import ask_codex_for_single_bug
from dotenv import dotenv_values

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

DEFECTS4J_PROJECTS = ['Cli', 'Closure', 'Codec', 'Collections', 'Compress', 'Csv', 'Gson',
                      'JacksonCore', 'JacksonDatabind', 'JacksonXml', 'Jsoup', 'JxPath', 'Lang', 'Math', 'Mockito', 'Time']


def checkout_bug(benchmark, working_directory, project, bug_id, version):
    bug_identifier = project + '_' + bug_id

    bug_path = os.path.join(working_directory,
                            "%s_%s_%s_%s" % (benchmark.name, project, bug_id, version))

    printlog('bug_identifier: ', bug_identifier)
    bug = benchmark.get_bug(bug_identifier)
    printlog('bug: ', bug)
    is_buggy_version = version == 'buggy'
    checkout_output = bug.checkout(bug_path, is_buggy_version)
    # print('checkout_output: ', checkout_output)
    # if checkout_output.count('Cannot determine how to apply patch') > 0:
    #     # git apply patch failed
    #     with open('/Users/pengyu/src/kth/llm-repair-them-all-results/patch-failed.txt', 'a') as f:
    #         f.write(bug_identifier + '\n')

    return bug


if __name__ == "__main__":
    args = parser.parse_args()
    benchmark = get_benchmark(args.benchmark)
    for project in DEFECTS4J_PROJECTS:
        for bug_id in range(1, DEFECTS4J_BUG_SIZE[project] + 1):
            printlog('checking out bug : project: ',
                     project, 'bug_id: ', bug_id)
            try:
                checkout_bug(benchmark, args.working_directory,
                             project, str(bug_id), 'buggy')
            except Exception as e:
                printlog('checkout bug failed: ', e)
                continue
