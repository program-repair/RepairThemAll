import os
import subprocess
import datetime
import json
import shutil

from config import JAVA7_HOME, JAVA8_HOME, JAVA_ARGS, DATA_PATH, REPAIR_ROOT
from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from core.RepairTool import RepairTool
from core.runner.RepairTask import RepairTask
from core.utils import add_repair_tool

class CapGen(RepairTool):
    """CapGen"""

    def __init__(self):
        super(CapGen, self).__init__("CapGen", "capgen")
        self.seed = 0

    def repair(self, repair_task):
        """"
        :type repair_task: RepairTask
        """
        bug = repair_task.bug

        if repair_task.benchmark.name not in ["Defects4J", "IntroClassJava"]:
            print("CapGen is only compatible with Defects4J and IntroClassJava")
            return

        root_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))

        if not os.path.exists(root_path):
            os.makedirs(root_path)
        bug_path = os.path.join(root_path, "%s_%s_buggy" % (bug.project, bug.bug_id))
        repair_task.working_directory = bug_path
        self.init_bug(bug, bug_path)

        try:
            # create config_local.txt file
            content = """workLoc=.
bugLoc =.
JDK7 = %s
task = RepairABug
project = %s
bid = %s
faultLocation = true
ingredientsExtraction = true
patchPrioritization = true
patchValidation = true
resultsAnalysis = true
""" % (JAVA7_HOME, bug.project, bug.bug_id)
            with open(os.path.join(root_path, "config_local.txt"), "w") as fd:
                fd.write(content)
            shutil.copy(self.jar, root_path + "/tool.jar")

            cmd = """cd %s;
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8 -Duser.language=en-US -Duser.country=US -Duser.language=en";
export LD_LIBRARY_PATH=%s/../lib/amd64/:%s/../jre/lib/amd64/:%s/scitools/bin/linux64/Java;
TZ="America/New_York"; export TZ;
export PATH="%s:%s:%s:$PATH";
export JAVA_HOME="%s";
time java %s -jar tool.jar;
""" % (root_path,
        JAVA8_HOME,
       JAVA8_HOME,
       os.path.join(DATA_PATH, "..", "libs"),
       JAVA8_HOME,
       os.path.join(DATA_PATH, "..", "libs", "scitools", "bin", "linux64"),
       os.path.join(REPAIR_ROOT, "benchmarks", "defects4j", "framework", "bin"),
        JAVA8_HOME,
        JAVA_ARGS)
            log_path = os.path.join(repair_task.log_dir(), "repair.log")
            if not os.path.exists(os.path.dirname(log_path)):
                os.makedirs(os.path.dirname(log_path))
            log = file(log_path, 'w')
            log.write(cmd)
            log.flush()
            subprocess.call(cmd, shell=True, stdout=log, stderr=subprocess.STDOUT)
        finally:
            cmd = "rm -rf %s;" % (root_path)
            subprocess.call(cmd, shell=True)
        pass

def init_capgen(args):
    return CapGen()

add_repair_tool("CapGen", init_capgen, 'Repair the bug with CapGen')