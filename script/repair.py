#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
try:
    import argcomplete
except:
    pass

from cli.repair_tools.astor import astor_args
from cli.repair_tools.dynamoth import dynamoth_args
from cli.repair_tools.nopol import nopol_args
from cli.repair_tools.npefix import npefix_args
from core.benchmarks.Bears import Bears
from core.benchmarks.BugDotJar import BugDotJar
from core.benchmarks.Defects4J import Defects4J
from core.benchmarks.IntroClassJava import IntroClassJava
from runner.RepairTask import RepairTask
from runner.runner import get_runner


def create_benchmark(benchmark):
    if benchmark.lower() == "defects4j":
        return Defects4J()
    elif benchmark.lower() == "introclassjava":
        return IntroClassJava()
    elif benchmark.lower() == "bugs.jar":
        return BugDotJar()
    elif benchmark.lower() == "bears":
        return Bears()
    return None


def completion_bug_id(prefix, parsed_args, **kwargs):
    results = []
    if parsed_args.benchmark is not None:
        benchmark = create_benchmark(parsed_args.benchmark)
        bugs = benchmark.get_bugs()
        for bug in bugs:
            results += ["%s-%s" % (bug.project, bug.bug_id)]
    return results


def initParser():
    parser = argparse.ArgumentParser(prog="repair", description='Repair bugs')

    bug_parser = argparse.ArgumentParser(add_help=False)
    bug_parser.add_argument("--benchmark", "-b", required=True, default="defects4j",
                            help="The benchmark to repair", choices=('Defects4J', 'IntroClassJava', 'Bugs.jar', 'Bears', 'QuixBugs'))
    bug_parser.add_argument("--id", "-i", required=True, help="The bug id").completer = completion_bug_id

    subparsers = parser.add_subparsers()

    astor_parser = subparsers.add_parser('jGenProg', help='Repair the bug with Astor', parents=[bug_parser])
    astor_args(astor_parser)

    npefix_parser = subparsers.add_parser('npefix', help='Repair the bug with NPEFix', parents=[bug_parser])
    npefix_args(npefix_parser)

    nopol_parser = subparsers.add_parser('Nopol', help='Repair the bug with Nopol', parents=[bug_parser])
    nopol_args(nopol_parser)

    dynamoth_parser = subparsers.add_parser('DynaMoth', help='Repair the bug with Dynamoth', parents=[bug_parser])
    dynamoth_args(dynamoth_parser)

    try:
        argcomplete.autocomplete(parser)
    except:
        pass

    return parser.parse_args()

if __name__ == "__main__":
    args = initParser()

    if "benchmark" in args:
        args.benchmark = create_benchmark(args.benchmark)
        args.bug = args.benchmark.get_bug(args.id)

    if "func" in args:
        tool = args.func(args)
        get_runner([RepairTask(tool, args.benchmark, args.bug)]).execute()
