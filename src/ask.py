import argparse
import time
from core.large_language_models.ask_codex import ask_codex_for_single_bug
from dotenv import dotenv_values

config = dotenv_values(".env")

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

FIXA_CONFIG = {
    'include_document': False,
    'include_comments': True,
    'compile': True,
    'sample': int(config.get('CODEX_SAMPLE_SIZE') or 1),
    'completion_ratio': 1.2,
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
            ask_codex_for_single_bug(args, str(bug_id), FIXA_CONFIG)
            time.sleep(12)
    elif args.project == None and args.id == None:
        # fix all bugs from all projects
        for project, bug_size in DEFECTS4J_BUG_SIZE.items():
            args.project = project
            for bug_id in range(1, bug_size + 1):
                ask_codex_for_single_bug(args, str(bug_id), FIXA_CONFIG)
                time.sleep(12)
    else:
        ask_codex_for_single_bug(args, args.id, FIXA_CONFIG)
