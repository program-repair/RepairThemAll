import json
import os
import shutil
import subprocess
import datetime

from config import WORKING_DIRECTORY, REPAIR_ROOT, JAVA7_HOME, JAVA8_HOME, JAVA_ARGS
from core.RepairTool import RepairTool
from core.utils import add_repair_tool
from core.runner.RepairTask import RepairTask

class Astor(RepairTool):
    """Astor"""

    def __init__(self, scope, name="Astor",
                 seed=0,
                 mode="jgenprog",
                 maxgen="1000000",
                 max_time=120,
                 population="1",
                 parameters="x:x",
                 stopfirst=True):
        super(Astor, self).__init__(name, "astor")
        self.seed = seed
        self.mode = mode
        self.maxgen = maxgen
        self.max_time = max_time
        self.scope = scope
        self.population = population
        self.parameters = parameters
        self.stopfirst = stopfirst

    def repair(self, repair_task):
        """"
        :type repair_task: RepairTask
        """
        bug = repair_task.bug
        bug_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))
        repair_task.working_directory = bug_path
        self.init_bug(bug, bug_path)

        jvm4testexecution = JAVA7_HOME
        if bug.compliance_level() > 7:
            jvm4testexecution = JAVA8_HOME
        try:
            classpath = bug.classpath()
            if classpath == "":
                classpath = '""'
            bin_folders = bug.bin_folders()[:]
            for folder in bug.bin_folders():
                if not os.path.exists(os.path.join(bug_path, folder)):
                    bin_folders.remove(folder)
            test_bin_folders = bug.test_bin_folders()[:]
            for folder in bug.test_bin_folders():
                if not os.path.exists(os.path.join(bug_path, folder)):
                    test_bin_folders.remove(folder)
            cmd = """cd %s;
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8 -Duser.language=en-US -Duser.country=US -Duser.language=en";
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
	-maxtime %d \\
	-stopfirst %s \\
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
       jvm4testexecution,
       jvm4testexecution,
       self.maxgen,
       self.max_time,
       "true" if self.stopfirst else "false",
       self.seed,
       self.scope,
       self.population,
       str(bug.compliance_level()),
       ":".join(bug.source_folders()),
       ":".join(bug.test_folders()),
       ":".join(bin_folders),
       ":".join(test_bin_folders),
       self.parameters,
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
            path_results = os.path.join(bug_path, "output_astor", "AstorMain-%s-%s" % (bug.project, bug.bug_id),
                                        "astor_output.json")
            if os.path.exists(path_results):
                repair_task.status = "FINISHED"
                shutil.copy(path_results,
                            os.path.join(repair_task.log_dir(), "detailed-result.json"))
                with open(path_results) as fd:
                    data = json.load(fd)
                    result = {
                        "repair_begin": self.repair_begin,
                        "repair_end": datetime.datetime.now().__str__(),
                        "patches": data["patches"]
                    }
                    repair_task.results = result
                    with open(os.path.join(repair_task.log_dir(), "result.json"), "w+") as fd2:
                        json.dump(result, fd2, indent=2)
                    if len(result['patches']) > 0:
                        repair_task.status = "PATCHED"
            else:
                repair_task.status = "ERROR"
            cmd = "rm -rf %s;" % (bug_path)
            subprocess.call(cmd, shell=True)
        pass

def init(args, name, mode):
    return Astor(name=name,
                    mode=mode,
                    maxgen=args.maxgen,
                    max_time=args.maxtime,
                    population=args.population,
                    scope=args.scope,
                    parameters=args.parameters,
                    seed=args.seed)


def cardumen_init(args):
    args.parameters += ":maxCombinationVariableLimit:true:maxVarCombination:1000"
    return init(args, "Cardumen", "cardumen")

def jgenprog_init(args):
    return init(args, "jGenProg", "jgenprog")

def jkali_init(args):
    return init(args, "jKali", "jkali")

def jMutRepair_init(args):
    return init(args, "jMutRepair", "jMutRepair")

def astor_args(parser):
    parser.add_argument("--seed", help="The random seed", default=0, type=int)
    parser.add_argument("--maxtime", help="Astor timeout", default=120, type=int)
    parser.add_argument("--population", help="Astor population", default=1, type=int)
    parser.add_argument("--maxgen", help="Astor maxgen", default=1000000, type=int)
    parser.add_argument("--scope", "-s", help="The scope of the ingredients", choices=("local", "package", "global"),
                        default="local")
    parser.add_argument("--parameters", "-p", help="Astor parameters", default="x:x")
    parser.add_argument("--dontstopfirst", help="Don't stop after the first bug",
                        action='store_false',
                        dest='stopfirst',
                        default=True)
    parser.add_argument('--version', action='version', version='Astor 26ee3dfc8b2d7ed4373f7cfe0d4bd5bcf31d9f28')
    pass

parser = add_repair_tool("jKali", jkali_init, 'Repair the bug with jKali')
astor_args(parser)

parser = add_repair_tool("jGenProg", jgenprog_init, 'Repair the bug with jGenProg')
astor_args(parser)

parser = add_repair_tool("jMutRepair", jMutRepair_init, 'Repair the bug with jMutRepair')
astor_args(parser)

parser = add_repair_tool("Cardumen", cardumen_init, 'Repair the bug with Cardumen')
astor_args(parser)