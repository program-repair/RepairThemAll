#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
try:
    import argcomplete
except:
    pass

from cli.repair_tools.astor import *
from cli.repair_tools.dynamoth import dynamoth_args
from cli.repair_tools.nopol import nopol_args
from cli.repair_tools.npefix import npefix_args
from cli.repair_tools.arja import *
from core.benchmarks.Bears import Bears
from core.benchmarks.BugDotJar import BugDotJar
from core.benchmarks.Defects4J import Defects4J
from core.benchmarks.IntroClassJava import IntroClassJava
from core.benchmarks.QuixBugs import QuixBugs
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
    elif benchmark.lower() == "quixbugs":
        return QuixBugs()
    return None


def completion_bug_id(prefix, parsed_args, **kwargs):
    results = []
    if parsed_args.benchmark is not None:
        benchmark = create_benchmark(parsed_args.benchmark)
        bugs = benchmark.get_bugs()
        for bug in bugs:
            results += ["%s-%s" % (bug.project, bug.bug_id)]
    return results


def init_parser():
    parser = argparse.ArgumentParser(prog="repair", description='Repair bugs')

    bug_parser = argparse.ArgumentParser(add_help=False)
    bug_parser.add_argument("--benchmark", "-b", required=True, default="defects4j",
                            help="The benchmark to repair", choices=('Defects4J', 'IntroClassJava', 'Bugs.jar', 'Bears', 'QuixBugs'))
    bug_parser.add_argument("--id", "-i", nargs='+', help="The bug id").completer = completion_bug_id

    subparsers = parser.add_subparsers()

    jgenprog_parser = subparsers.add_parser('jGenProg', help='Repair the bug with jGenProg', parents=[bug_parser])
    jgenprog_args(jgenprog_parser)

    jkali_parser = subparsers.add_parser('jKali', help='Repair the bug with jKali', parents=[bug_parser])
    jkali_args(jkali_parser)

    jMutRepair_parser = subparsers.add_parser('jMutRepair', help='Repair the bug with jMutRepair', parents=[bug_parser])
    jMutRepair_args(jMutRepair_parser)

    npefix_parser = subparsers.add_parser('NPEFix', help='Repair the bug with NPEFix', parents=[bug_parser])
    npefix_args(npefix_parser)

    nopol_parser = subparsers.add_parser('Nopol', help='Repair the bug with Nopol', parents=[bug_parser])
    nopol_args(nopol_parser)

    dynamoth_parser = subparsers.add_parser('DynaMoth', help='Repair the bug with Dynamoth', parents=[bug_parser])
    dynamoth_args(dynamoth_parser)

    arja_parser = subparsers.add_parser('Arja', help='Repair the bug with Arja', parents=[bug_parser])
    arja_args(arja_parser)

    rsrepair_parser = subparsers.add_parser('RSRepair', help='Repair the bug with RSRepair', parents=[bug_parser])
    rsrepair_args(rsrepair_parser)

    genprog_parser = subparsers.add_parser('GenProg', help='Repair the bug with GenProg (from Arja)', parents=[bug_parser])
    genprog_args(genprog_parser)

    kali_parser = subparsers.add_parser('Kali', help='Repair the bug with Kali (from Arja)', parents=[bug_parser])
    kali_args(kali_parser)

    try:
        argcomplete.autocomplete(parser)
    except:
        pass

    return parser.parse_args()


if __name__ == "__main__":
    args = init_parser()

    if "benchmark" in args:
        args.benchmark = create_benchmark(args.benchmark)

        tasks = []
        bugs = args.benchmark.get_bugs()
        if args.id is not None:
            bugs = []
            for bug_id in args.id:
                bugs.append(args.benchmark.get_bug(bug_id))

        for bug in bugs:
            args.bug = bug

            tool = args.func(args)
            tasks.append(RepairTask(tool, args.benchmark, bug))

        get_runner(tasks).execute()
