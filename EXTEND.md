# Extending RepairThemAll to add support for different repair tools and benchmarks of bugs 

### To add a new benchmark

1. Put your benchmark folder in `./benchmarks`.

2. Create a new file in `script/core/benchmarks/` that contains the following content:

```py
from core.Benchmark import Benchmark

class <benchmark_name>(Benchmark):
    """<benchmark_name> Benchmark"""

    def __init__(self):
        super(<benchmark_name>, self).__init__("<benchmark_name>")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "<benchmark_name>")
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

add_benchmark("<benchmark_name>", <benchmark_name>)
```

3. Go to `script/core/utils.py` and import your benchmark in the end of the file (like `import core.benchmarks.<benchmark_name>`).

### To add a new repair tool

1. Add the binary (jar file) of your repair tool in `./repair_tools`.

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

class <repair_tool_name>(RepairTool):
    """<repair_tool_name>"""

    def __init__(self, name="<repair_tool_name>"):
        super(<repair_tool_name>, self).__init__(name, "<repair_tool_name>")
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
    return <repair_tool_name>()

def _args(parser):
    # additional argument for the repair tool
    parser.add_argument("--argument", help="description", default=100)
    pass

parser = add_repair_tool("<repair_tool_name>", init, 'Repair the bug with <repair_tool_name>')
_args(parser)
```

3. Go to `script/core/utils.py` and import your repair tool in the end of the file (like `import core.repair_tools.<repair_tool_name>`).

4. Add the file `<repair_tool_name>.json` into folder `data/repair_tools/`.
The file must have the following content:

```
{
	"name": "<repair_tool_name>",
	"version": "x.y.z",
	"jar": "<repair_tool_name>.jar",
	"main": "<main of the class containing the main (the entry point of the tool)>"
}

```

