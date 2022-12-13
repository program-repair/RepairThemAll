import os
import argparse

from core.utils import get_benchmark

parser = argparse.ArgumentParser(prog="checkout", description='Checkout bug')
parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                    help="The benchmark to repair")
parser.add_argument("--id", "-i", required=True, help="The bug id")
parser.add_argument("--version", "-v",
                    required=False, help="buggy (default) or fixed version")
parser.add_argument("--working_directory", "-w",
                    required=True, help="The working directory")

if __name__ == "__main__":
    args = parser.parse_args()
    args.benchmark = get_benchmark(args.benchmark)
    bug = args.benchmark.get_bug(args.id)
    if args.version == "fixed":
        buggy_version = False
        version_str = "fixed"
    else:
        buggy_version = True
        version_str = "buggy"
    bug_path = os.path.join(args.working_directory,
                            "%s_%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id, version_str))
    bug.checkout(bug_path, buggy_version)  # buggy or fixed
    print('--bug--')
    print(bug)
    print(bug_path)
    print('--compile--')
    bug.compile()
    print('--end---')
