import os
import shutil
import json
import subprocess
import datetime

from config import JAVA8_HOME
from config import JAVA_ARGS
from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from config import Z3_PATH
from core.RepairTool import RepairTool
from core.runner.RepairTask import RepairTask
from core.utils import add_repair_tool


class Nopol(RepairTool):
    """Nopol"""

    def __init__(self, name="Nopol", mode="repair", oracle="angelic", statement_type="pre_then_cond", seed=7, synthesis="smt"):
        super(Nopol, self).__init__(name, "nopol")
        self.solver = self.data["solver"]
        self.synthesis = synthesis
        self.flocal = "gzoltar"
        self.mode = mode
        self.oracle = oracle
        self.statement_type = statement_type
        self.seed = seed

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
            classpath = ":".join(bug.bin_folders() + bug.test_bin_folders())
            if classpath != ":":
                classpath += ":" 
            classpath += bug.classpath()
            classpath += ":" + self.jar
            cmd = """cd %s;
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8 -Duser.language=en-US -Duser.country=US -Duser.language=en";
TZ="America/New_York"; export TZ;
export PATH="%s:$PATH";
export JAVA_HOME="%s";
time java %s -cp %s:%s/../lib/tools.jar %s \\
	--mode %s \\
	--type %s \\
	--oracle %s \\
	--synthesis %s \\
	--flocal %s \\
	--json \\
	--solver %s \\
	--solver-path %s \\
	--complianceLevel %s \\
	--source %s \\
	--classpath "%s";
	echo "\\n\\nNode: `hostname`\\n";
	echo "\\n\\nDate: `date`\\n";
""" % (bug_path,
       JAVA8_HOME,
       JAVA8_HOME,
       JAVA_ARGS,
       self.jar,
       JAVA8_HOME,
       self.main,
       self.mode,
       self.statement_type,
       self.oracle,
       self.synthesis,
       self.flocal,
       self.solver,
       os.path.join(Z3_PATH, "z3"),
       str(bug.compliance_level()),
       ":".join(bug.source_folders()),
       classpath)
            log_path = os.path.join(repair_task.log_dir(), "repair.log")
            if not os.path.exists(os.path.dirname(log_path)):
                os.makedirs(os.path.dirname(log_path))
            log = file(log_path, 'w')
            log.write(cmd)
            log.flush()
            subprocess.call(cmd, shell=True, stdout=log, stderr=subprocess.STDOUT)
            with open(log_path) as data_file:
                return data_file.read()
        finally:
            path_results = os.path.join(bug_path, "output.json")
            if os.path.exists(path_results):
                repair_task.status = "FINISHED"
                shutil.copy(path_results, os.path.join(repair_task.log_dir(), "detailed-result.json"))
                with open(path_results) as fd:
                    repair_task.results = json.load(fd)
                    result = {
                        "repair_begin": self.repair_begin,
                        "repair_end": datetime.datetime.now().__str__(),
                        'patches': []
                    }
                    if 'patch' in repair_task.results:
                        result['patches'] = repair_task.results["patch"]
                    with open(os.path.join(repair_task.log_dir(), "result.json"), "w") as fd2:
                        json.dump(result, fd2, indent=2)
                    if len(result['patches']) > 0:
                        repair_task.status = "PATCHED"
            else:
                repair_task.status = "ERROR"
            cmd = "rm -rf %s;" % (bug_path)
            #subprocess.call(cmd, shell=True)
        pass

def init(args):
    return Nopol(seed=args.seed, statement_type=args.statement_type)

def init_dynamoth(args):
    return Nopol(name="DynaMoth", seed=args.seed, statement_type=args.statement_type, synthesis="dynamoth")

def nopol_args(parser):
    parser.add_argument("--statement-type", "-t",
                        help="The targeted statement", default="pre_then_cond", choices=("condition", "precondition", "pre_then_cond"))
    parser.add_argument('--version', action='version', version='Astor 7ba58a78d')                        
    parser.add_argument("--seed", "-s", help="The random seed", default=7, type=int)
    pass

parser = add_repair_tool("Nopol", init, 'Repair the bug with Nopol')
nopol_args(parser)

parser = add_repair_tool("Dynamoth", init_dynamoth, 'Repair the bug with Dynamoth')
nopol_args(parser)