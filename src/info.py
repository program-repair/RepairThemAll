import os
import argparse
import json
import shutil

from config import WORKING_DIRECTORY
from core.utils import get_benchmark
# from core.runner.RepairTask import RepairTask

parser = argparse.ArgumentParser(prog="checkout", description='Checkout bug')
parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                    help="The benchmark to repair")
parser.add_argument("--id", "-i", help="The bug id")

if __name__ == "__main__":
    args = parser.parse_args()
    args.benchmark = get_benchmark(args.benchmark)

    if args.id is not None:
        bug = args.benchmark.get_bug(args.id)

        bug_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id))
        bug.checkout(bug_path)
        bug.compile()

        print(json.dumps({
            "failingTests": bug.failing_tests(),
            "sources": bug.source_folders(),
            "tests": bug.test_folders(),
            "bins": bug.bin_folders(),
            "testBins": bug.test_bin_folders(),
            "classpath": bug.classpath(),
            "complianceLevel": bug.compliance_level(),
        }, indent=1, sort_keys=True))

        shutil.rmtree(bug_path)
    else:
        print(json.dumps(args.benchmark.get_bugs(), default=lambda x: {
              "project": x.project, "bug_id": x.bug_id, "benchmark": x.benchmark.name}, indent=1, sort_keys=True))
