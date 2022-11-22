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
bug_parser.add_argument(
    "--endTime", help="Specify an hour to stop the execution (hh:mm)", dest="end_time", default=None)

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
    parser = subparsers.add_parser(
        name, help=description, parents=[bug_parser])
    parser.set_defaults(func=clas)
    return parser


def getGridTime(timeout, overhead=0.33):
    ''' computes the timeout of the grid based on the timeout (from the tool) received as parameter.
    Moreover it adds an overhead with is a percentage of the original timeout'''
    timetool = int(timeout)
    timetooloverhead = timetool + (timetool * overhead)
    hr_st = str(int(timetooloverhead // 60))
    minutes = int(timetooloverhead % 60)
    mt_st = str(minutes) if minutes >= 10 else ("0" + str(minutes))
    timestring = hr_st + ":" + mt_st
    return timestring


import core.benchmarks.Bears
import core.benchmarks.BugDotJar
import core.benchmarks.Defects4J

# import core.repair_tools.Astor
# import core.repair_tools.Nopol
# import core.repair_tools.NPEFix
