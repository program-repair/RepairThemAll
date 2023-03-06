
import argparse
import time
from dotenv import dotenv_values
from core.large_language_models.ask_codex_bugs_jar import ask_codex_for_single_bug

from core.utils import get_benchmark

parser = argparse.ArgumentParser(
    prog="ask", description='Checkout and fix the bug by pre-trained large language model')
parser.add_argument("--model", "-m", required=True,
                    help="The pre-trained large language model (for example, codex)")
parser.add_argument("--benchmark", "-b", required=True, default="Bugs.jar",
                    help="The benchmark to repair")
parser.add_argument("--project", "-p", required=False,
                    help="The project name (case sensitive)")
parser.add_argument("--id", "-i", required=False, help="The bug id")
parser.add_argument("--working_directory", "-w",
                    required=True, help="The working directory")

config = dotenv_values(".env")

FIXA_CONFIG = {
    'include_document': False,
    'include_comments': True,
    'compile': True,
    'sample': int(config.get('CODEX_SAMPLE_SIZE') or 1),
    'completion_ratio': 1.2,
}

BUGS_DOT_JAR_PROJECTS = [
    'accumulo', 'commons-math', 'jackrabbit-oak', 'wicket'
]

BUG_LISTS = {
    'accumulo': [12, 16, 26, 27, 32, 33, 37, 38, 46, 60, 67],
    'commons-math': [4, 6, 9, 11, 17, 19, 20, 24, 32, 36, 40, 47, 48, 56, 60, 62, 63, 66, 67, 68, 69, 75, 86, 88, 92, 94, 95, 103, 106, 111, 114, 119, 120, 121, 127, 134, 135, 144, 147],
    'jackrabbit-oak': [2, 9, 12, 16, 17, 26, 34, 40, 49, 59, 67, 68, 80, 81, 90, 91, 95, 97, 98, 102, 105, 106, 108, 109, 113, 116, 128, 134, 135, 137, 140, 146, 159, 160, 162, 165, 166, 167, 168, 174, 175, 179, 183, 189, 193, 194, 200, 202, 219, 220, 229, 234, 237, 238, 240, 242, 249, 254, 260],
    'wicket': [6, 9, 19, 23, 32, 35, 45, 47, 56, 62, 63, 68, 70, 71, 73, 91, 93, 98, 109, 111, 140, 146, 147, 155, 157, 185, 186, 187, 194, 196, 208, 215, 216, 218, 223, 229, 233, 239, 241, 249, 251, 254, 261, 263, 270, 272, 279, 285, 288],
}


def process_bugs_dot_jar_codex(args, bug_id, fixa_config):
    benchmark = get_benchmark(args.benchmark)
    ask_codex_for_single_bug(benchmark, args, bug_id, fixa_config)


if __name__ == '__main__':
    args = parser.parse_args()

    if args.project is None:
        for project in BUGS_DOT_JAR_PROJECTS:
            args.project = project
            for bug_id in BUG_LISTS[args.project]:
                process_bugs_dot_jar_codex(args, bug_id, FIXA_CONFIG)
                time.sleep(12)
    elif args.project != None and args.id == None:
        for bug_id in BUG_LISTS[args.project]:
            process_bugs_dot_jar_codex(args, bug_id, FIXA_CONFIG)
            time.sleep(12)
    else:
        process_bugs_dot_jar_codex(args, args.id, FIXA_CONFIG)
        time.sleep(12)
