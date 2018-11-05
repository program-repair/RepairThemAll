import os
import shutil
import json
import subprocess

from config import JAVA8_HOME
from config import JAVA_ARGS
from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from config import Z3_PATH
from core.RepairTool import RepairTool
from runner.RepairTask import RepairTask

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
        self.init_bug(bug, bug_path)
        try:
            cmd = """cd %s;
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;
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
       Z3_PATH,
       str(bug.compliance_level()),
       ":".join(bug.source_folders()),
       bug.classpath())
            logPath = os.path.join(OUTPUT_PATH, bug.benchmark.name, bug.project, str(bug.bug_id), self.name,
                                   str(self.seed), "stdout.log.full")
            if not os.path.exists(os.path.dirname(logPath)):
                os.makedirs(os.path.dirname(logPath))
            log = file(logPath, 'w')
            log.write(cmd)
            subprocess.call(cmd, shell=True, stdout=log, stderr=subprocess.STDOUT)
            with open(logPath) as data_file:
                return data_file.read()
        finally:
            path_results = os.path.join(bug_path, "output.json")
            if os.path.exists(path_results):
                repair_task.status = "FINISHED"
                shutil.copy(path_results,
                            os.path.join(OUTPUT_PATH, bug.benchmark.name, bug.project, str(bug.bug_id), self.name,
                                         str(self.seed), "result.json"))
                with open(path_results) as fd:
                    repair_task.results = json.load(fd)
                    if len(repair_task.results['patches']) > 0:
                        repair_task.status = "PATCHED"

            else:
                repair_task.status = "ERROR"
            cmd = "rm -rf %s;" % (bug_path)
            subprocess.call(cmd, shell=True)
        pass
