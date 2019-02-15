import os
import argparse

from core.utils import get_benchmark

parser = argparse.ArgumentParser(prog="checkout", description='Checkout bug')
parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                        help="The benchmark to repair")
parser.add_argument("--id", "-i", required=True, help="The bug id")
parser.add_argument("--working_directory", "-w", required=True, help="The working directory")

if __name__ == "__main__":
    args = parser.parse_args()
    args.benchmark = get_benchmark(args.benchmark)
    bug = args.benchmark.get_bug(args.id)
    bug_path = os.path.join(args.working_directory,
                            "%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id))
    bug.checkout(bug_path)