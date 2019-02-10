import os
import subprocess
import datetime
import json
import shutil

from config import JAVA8_HOME
from config import JAVA_ARGS
from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from core.RepairTool import RepairTool
from core.utils import add_repair_tool
from core.runner.RepairTask import RepairTask

class NPEFix(RepairTool):
    """NPEFix"""

    def __init__(self, name="NPEFix", iteration=100):
        super(NPEFix, self).__init__(name, "npefix")
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
            classpath = ":".join(bug.bin_folders() + bug.test_bin_folders())
            classpath += ":" + bug.classpath()
            compliance_level = bug.compliance_level()
            if compliance_level < 5:
                # NPEFix metaprogram is not compatible below Java 1.5
                compliance_level = 5
            cmd = """cd %s;
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8 -Duser.language=en-US -Duser.country=US -Duser.language=en";
TZ="America/New_York"; export TZ;
export PATH="%s:$PATH";
export JAVA_HOME="%s";
time java %s -cp %s %s \\
    --test %s \\
    --iteration %s \\
	--complianceLevel %s \\
	--workingdirectory . \\
	--source %s \\
	--classpath %s;
	echo "\\n\\nNode: `hostname`\\n";
	echo "\\n\\nDate: `date`\\n";
""" % (bug_path,
        JAVA8_HOME,
        JAVA8_HOME,
        JAVA_ARGS,
        self.jar,
        self.main,
        ":".join(bug.failing_tests()),
        self.iteration,
        str(compliance_level),
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
            result = {
                "repair_begin": self.repair_begin,
                "repair_end": datetime.datetime.now().__str__(),
                "patches": []
            }
            repair_task.status = "FINISHED"
            output_file = None
            for d in os.listdir(bug_path):
                if "patches_" in d:
                    output_file = d
                    break

            path_output = os.path.join(bug_path, output_file) if output_file is not None else None
            if path_output is not None and os.path.exists(path_output):
                shutil.copy(path_output, os.path.join(repair_task.log_dir(), "detailed-result.json"))
                with open(path_output) as fd:
                    data = json.load(fd)
                    if 'executions' in data:
                        executions = data['executions']
                        for execution in executions:
                            if not execution['result']['success'] or 'decisions' not in execution:
                                continue
                            result['patches'].append({
                                'diff': execution['diff'],
                                'locations': execution['locations']
                            })
                pass
            else:
                repair_task.status = "ERROR"
            repair_task.results = result
            if len(result['patches']) > 0:
                repair_task.status = "PATCHED"
            with open(os.path.join(repair_task.log_dir(), "result.json"), "w+") as fd2:
                json.dump(result, fd2, indent=2)
            cmd = "rm -rf %s;" % (bug_path)
            subprocess.call(cmd, shell=True)
        pass


def init(args):
    return NPEFix(iteration=args.iteration)


def npefix_args(parser):
    parser.add_argument('--version', action='version', version='Astor 403445b9a')
    parser.add_argument("--iteration", help="The maximum number of NPEFix iteration", default=100, type=int)
    pass

parser = add_repair_tool('NPEFix', init, 'Repair the bug with NPEFix')
npefix_args(parser)