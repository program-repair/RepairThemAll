import argparse

from core.utils import get_benchmark

parser = argparse.ArgumentParser(prog="print_bugs_available", description='Print the bugs available from a benchmark')
parser.add_argument("--benchmark", "-b", required=True, help="The name of the benchmark {Bears, Bugs.jar, Defects4J, IntroClassJava, QuixBugs}")

if __name__ == "__main__":
    args = parser.parse_args()
    args.benchmark = get_benchmark(args.benchmark)

    bugs = args.benchmark.get_bugs()
    for bug in bugs:
	if bug.bug_id:
    		print bug.project + '-' + str(bug.bug_id)
	else:
		print bug.project

