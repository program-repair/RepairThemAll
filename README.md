# RepairThemAll

RepairThemAll is a framework that allows the execution of automatic program repair tools on benchmarks of bugs by providing an abstraction around the repair tools and the benchmarks.

If you use RepairThemAll, please cite our paper:

```bibtex
@inproceedings{RepairThemAll2019,
  author    = {Thomas Durieux and Fernanda Madeiral and Matias Martinez and Rui Abreu},
  title     = {{Empirical Review of Java Program Repair Tools: A Large-Scale Experiment on 2,141 Bugs and 23,551 Repair Attempts}},
  booktitle = {Proceedings of the 27th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE '19)},
  year      = {2019},
  url       = {https://arxiv.org/abs/1905.11973}
}
```

## Current support

### Benchmarks of bugs

| Benchmark      | # Projects | # Bugs |
| -------------- | -----------| -------|
| Bears          |         71 |    251 |
| Bugs.jar       |          8 |   1158 |
| Defects4J      |          6 |    395 |
| IntroClassJava |          6 |    297 |
| QuixBugs       |         40 |     40 |
| **Total**      |        130 |   2051 |

### Repair tools

1. Nopol
2. DynaMoth
3. NPEFix
4. jGenProg
5. jKali
6. jMutRepair
7. Cardumen
8. ARJA
9. GenProg-A
10. RSRepair-A
11. Kali-A

## Usage

### Requirements

1. Linux or Mac
2. Java 7
3. Java 8
4. Python 2
5. Maven
6. Ant

### Executing repair tools

1. Clone this repository with `git clone --recursive https://github.com/program-repair/RepairThemAll.git`

2. Init the repository with `./init.sh`.

3. Go to `script/config.py` and update the configuration for your machine (java home and working directory).

4. Use `python script/repair.py` to run the repair tools on the benchmarks.

General usage:

```bash
python script/repair.py {astor,npefix,nopol,dynamoth}
    --benchmark [Defects4J, IntroclassJava, Bugs.jar, Bears, QuixBugs]
    --id <bug_id> # optional, if not specified all the bugs of the benchmark will be executed. The format is specific for each benchmark
```

## Extending RepairThemAll

### To add a new benchmark

1. Put your benchmark folder in `./benchmarks`.

2. Create a new file in `script/core/benchmarks/` that contains the following content:

```py
from core.Benchmark import Benchmark

class BenchmarkName(Benchmark):
    """<name> Benchmark"""

    def __init__(self):
        super(BenchmarkName, self).__init__(<name>)
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", <name>)
        self.bugs = None
        self.get_bugs()

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs
        self.bugs = []
        # get all the bugs of the benchmark
        return self.bugs

    def get_bug(self, bug_id):
        # get a bug based on its id
        return None

    def checkout(self, bug, working_directory):
        # checkout a bug
        pass


    def compile(self, bug, working_directory):
        # compile a bug
        pass

    def run_test(self, bug, working_directory):
        # run the test of a bug
        pass

    def failing_tests(self, bug):
        tests = [...] # list of failing class
        return tests

    def source_folders(self, bug):
        return [os.path.join("src", "main", "java")]

    def test_folders(self, bug):
        return [os.path.join("src", "test", "java")]

    def bin_folders(self, bug):
        return [os.path.join("target", "classes")]

    def test_bin_folders(self, bug):
        return [os.path.join("target", "test-classes")]

    def classpath(self, repair_task):
        classpath = []
        return ":".join(classpath)

    def compliance_level(self, bug):
        return 8

add_benchmark(<name>, BenchmarkName)
```

3. Go to `script/core/utils.py` and import your benchmark in the end of the file (like `import core.benchmarks.BenchmarkName`).

### To add a new repair tool

1. Add the binary of your repair tool in `./repair_tools`.

2. Create a new file in `script/core/repair_tools/` that contains the following content:

```py
import os
import subprocess
import datetime
import json
import shutil

from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from core.RepairTool import RepairTool
from core.utils import add_repair_tool
from core.runner.RepairTask import RepairTask

class Tool(RepairTool):
    """Tool"""

    def __init__(self, name=<repair_name>):
        super(Tool, self).__init__(name, <repair_name>)
        self.seed = 0
        self.iteration = iteration

    def repair(self, repair_task):
        """"
        :type repair_task: RepairTask
        """
        bug = repair_task.bug
        bug_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))
        repair_task.working_directory = bug_path
        self.init_bug(bug, bug_path)

        try:
            failing_tests =  bug.failing_tests(),
            sources = bug.source_folders(),
            tests = bug.test_folders(),
            bin_folders = bug.bin_folders(),
            test_bin_folders = bug.test_bin_folders(),
            classpath = bug.classpath(),
            compliance_level = bug.compliance_level(),

            # run the repair tool
        finally:
            result = {
                "repair_begin": self.repair_begin,
                "repair_end": datetime.datetime.now().__str__(),
                "patches": []
            }
            repair_task.status = "FINISHED"
            
            # normalize the output in result
            with open(os.path.join(repair_task.log_dir(), "result.json"), "w+") as fd2:
                json.dump(result, fd2, indent=2)
            shutil.rmtree(bug_path)
        pass



def init(args):
    return Tool()

def _args(parser):
    # additional argument for the repair tool
    parser.add_argument("--argument", help="description", default=100)
    pass

parser = add_repair_tool(<repair_name>, init, 'Repair the bug with <repair_name>')
_args(parser)
```

3. Go to `script/core/utils.py` and import your repair tool in the end of the file (like `import core.repair_tools.Tool`).
