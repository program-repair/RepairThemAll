import json
import os
import shutil
import subprocess

from config import WORKING_DIRECTORY, REPAIR_ROOT, JAVA7_HOME, JAVA8_HOME, JAVA_ARGS, OUTPUT_PATH
from core.RepairTool import RepairTool


class Astor(RepairTool):
    """Astor"""

    def __init__(self, scope, name="Astor", seed=0, mode="jgenprog", maxgen="1000000", population="1",
                 parameters="x:x"):
        super(Astor, self).__init__(name, "astor")
        self.seed = seed
        self.mode = mode
        self.maxgen = maxgen
        self.scope = scope
        self.population = population
        self.parameters = parameters

    def repair(self, repair_task):
        """"
        :type repair_task: RepairTask
        """
        bug = repair_task.bug
        bug_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))
        self.init_bug(bug, bug_path)
        try:
            classpath = bug.classpath()
            cmd = """cd %s;
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;
TZ="America/New_York"; export TZ;
export PATH="%s:$PATH";
export JAVA_HOME="%s";
time java %s -cp %s %s \\
	-mode %s \\
	-location . \\
	-id %s \\
	-failing %s \\
	-jvm4testexecution %s \\
	-jvm4evosuitetestexecution %s \\
	-maxgen %s \\
	-maxtime 10 \\
	-stopfirst true \\
	-seed %s \\
	-scope %s \\
	-population %s \\
	-javacompliancelevel %s \\
	-srcjavafolder %s \\
	-srctestfolder %s \\
	-binjavafolder %s \\
	-bintestfolder %s \\
	-parameters %s \\
	-dependencies %s;
	echo "\\n\\nNode: `hostname`\\n";
	echo "\\n\\nDate: `date`\\n";
""" % (bug_path,
       JAVA8_HOME,
       JAVA8_HOME,
       JAVA_ARGS,
       os.path.join(REPAIR_ROOT, "libs", "jtestex7.jar") + ":" + self.jar,
       self.main,
       self.mode,
       "%s-%s" % (bug.project, bug.bug_id),
       ":".join(bug.failing_tests()),
       JAVA8_HOME,
       JAVA8_HOME,
       self.maxgen,
       self.seed,
       self.scope,
       self.population,
       str(bug.compliance_level()),
       ":".join(bug.source_folders()),
       ":".join(bug.test_folders()),
       ":".join(bug.bin_folders()),
       ":".join(bug.test_bin_folders()),
       self.parameters,
       classpath)
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
            path_results = os.path.join(bug_path, "output_astor", "AstorMain-%s-%s" % (bug.project, bug.bug_id),
                                        "astor_output.json")
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
