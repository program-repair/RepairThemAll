import argparse
import os

benchmarks = {}
repair_tools = {}

parser = argparse.ArgumentParser(prog="repair", description='Repair bugs')
bug_parser = argparse.ArgumentParser(add_help=False)
bug_parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                        help="The benchmark to repair")
bug_parser.add_argument("--continue", 
                    help="Continue the previous execution", 
                    action='store_true',
                    dest='continue_execution',
                    default=False)
bug_parser.add_argument("--endTime", help="Specify an hour to stop the execution (hh:mm)", dest="end_time", default=None)

bug_parser.add_argument("--id", "-i", nargs='+', help="The bug id")

subparsers = parser.add_subparsers()

def add_benchmark(name, clas): 
    benchmarks[name] = clas

def get_benchmark(benchmark):
    """
    :return Benchmark
    """
    for b in benchmarks:
        if benchmark.lower() == b.lower():
            return benchmarks[b]()
    return None

def add_repair_tool(name, clas, description):
    repair_tools[name] = clas
    parser = subparsers.add_parser(name, help=description, parents=[bug_parser])
    parser.set_defaults(func=clas)
    return parser


import core.benchmarks.Bears
import core.benchmarks.BugDotJar
import core.benchmarks.Defects4J
import core.benchmarks.IntroClassJava
import core.benchmarks.QuixBugs

import core.repair_tools.Arja
import core.repair_tools.Astor
import core.repair_tools.CapGen
import core.repair_tools.LSRepair
import core.repair_tools.Nopol
import core.repair_tools.NPEFix