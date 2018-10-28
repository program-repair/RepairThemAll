import argparse

from cli.info import info_args
from cli.repair_tools.astor import astor_args
from cli.repair_tools.npefix import npefix_args
from cli.repair_tools.nopol import nopol_args
from cli.repair_tools.dynamoth import dynamoth_args

from core.Bug import Bug
from core.benchmarks.Defects4J import Defects4J
from core.benchmarks.IntroClassJava import IntroClassJava


def initParser():
    parser = argparse.ArgumentParser(prog="repair", description='Repair Defects4J\'s bugs')

    bug_parser = argparse.ArgumentParser(add_help=False)
    bug_parser.add_argument("--benchmark", "-b", required=True, default="defects4j", help="The benchmark to repair [defects4j, introclassjava, bugs.jar]")
    bug_parser.add_argument("--project", "-p", required=True, help="The project name")
    bug_parser.add_argument("--id", "-i", required=True, help="The bug id")

    subparsers = parser.add_subparsers()

    astor_parser = subparsers.add_parser('astor', help='Repair the bug with Astor', parents=[bug_parser])
    astor_args(astor_parser)

    npefix_parser = subparsers.add_parser('npefix', help='Repair the bug with NPEFix', parents=[bug_parser])
    npefix_args(npefix_parser)

    nopol_parser = subparsers.add_parser('nopol', help='Repair the bug with Nopol', parents=[bug_parser])
    nopol_args(nopol_parser)

    dynamoth_parser = subparsers.add_parser('dynamoth', help='Repair the bug with Dynamoth', parents=[bug_parser])
    dynamoth_args(dynamoth_parser)

    return parser.parse_args()

def get_bug(args):
    project = args.project
    if project[0].lower() == project[0]:
        project = project[0].upper() + project[1:]
    id = int(args.id)
    return Bug(args.benchmark, project, id)

if __name__ == "__main__":
    args = initParser()
    if args.benchmark.lower() == "defects4j":
        args.benchmark = Defects4J()
    elif args.benchmark.lower() == "introclassjava":
        args.benchmark = IntroClassJava()
    elif args.benchmark.lower() == "bugs.jar":
        args.benchmark = Defects4J()
    args.bug = get_bug(args)
    args.func(args)
