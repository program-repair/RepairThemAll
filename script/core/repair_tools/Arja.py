import json
import os
import shutil
import subprocess

from config import WORKING_DIRECTORY, REPAIR_ROOT, JAVA8_HOME, JAVA_ARGS, OUTPUT_PATH
from core.RepairTool import RepairTool


def to_absolute(root, folders):
    absolute_folders = []
    for folder in folders:
        if os.path.exists(os.path.join(root, folder)):
            absolute_folders.append(os.path.join(root, folder))
    return absolute_folders


class Arja(RepairTool):
    """Arja"""

    def __init__(self, name="Arja",
                 seed=0,
                 mode="Arja"):
        super(Arja, self).__init__(name, "arja")
        self.seed = seed
        self.mode = mode

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
            classpath = bug.classpath(repair_task)
            if classpath == "":
                classpath = '""'
            bin_folders = to_absolute(bug_path, bug.bin_folders())
            test_bin_folders = to_absolute(bug_path, bug.test_bin_folders())
            sources = to_absolute(bug_path, bug.source_folders())
            cmd = """cd %s;
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;
TZ="America/New_York"; export TZ;
export PATH="%s:$PATH";
export JAVA_HOME="%s";
time java %s -cp %s %s \\
	%s \\
	-DexternalProjRoot /home/tdurieux/git/arja/external \\
	-DsrcJavaDir %s \\
	-DbinJavaDir %s \\
	-DbinTestDir %s \\
	-Ddependences %s;
	echo "\\n\\nNode: `hostname`\\n";
	echo "\\n\\nDate: `date`\\n";
""" % (bug_path,
        JAVA8_HOME,
        JAVA8_HOME,
        JAVA_ARGS,
        os.path.join(REPAIR_ROOT, "libs", "jmetal.jar") + ":" + self.jar,
        self.main,
        self.mode,
        ":".join(sources),
        ":".join(bin_folders),
        ":".join(test_bin_folders),
        classpath)
            log_path = os.path.join(OUTPUT_PATH, bug.benchmark.name, bug.project, str(bug.bug_id), self.name,
                                    str(self.seed), "repair.log")
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
                "patches": []
            }
            repair_task.status = "FINISHED"
            output_folder = None
            for d in os.listdir(bug_path):
                if "patches_" in d:
                    output_folder = d
                    break

            path_results = os.path.join(bug_path, output_folder) if output_folder is not None else None
            if path_results is not None and os.path.exists(path_results):
                for f in os.listdir(path_results):
                    path_f = os.path.join(path_results, f)
                    if not os.path.isfile(path_f) or ".txt" not in f:
                        continue
                    with open(path_f) as fd:
                        str_patches = fd.read().split(
                            "**************************************************")
                        edits = []
                        for str_patch in str_patches:
                            splitted_patch = str_patch.strip().split("\n")
                            info_line = splitted_patch[0].split(" ")
                            if info_line[0] == "Evaluations:" or "EstimatedTime:" == info_line[0]:
                                continue

                            is_kali = "." in info_line[-1]
                            if not is_kali:
                                edit = {
                                    "type": info_line[1],
                                    "path": " ".join(info_line[2:-1]).replace("%s/" % bug_path, ""),
                                    "line": int(info_line[-1])
                                }
                                content = "%s\n" % splitted_patch[2]
                                for line in splitted_patch[3:]:
                                    if line == "Seed:":
                                        edit["faulty"] = content.strip()
                                        content = ""
                                    else:
                                        content += "%s\n" % line
                                edit["seed"] = content.strip()
                            else:
                                edit = {
                                    "type": "%s %s" % (info_line[0], info_line[1]),
                                    "path": " ".join(info_line[2:-2]).replace("%s/" % bug_path, ""),
                                    "line": int(info_line[-2]),
                                    "faulty": "\n".join(splitted_patch[1:])
                                }

                            edits.append(edit)
                        result["patches"].append({
                            "edits": edits
                        })
                with open(os.path.join(OUTPUT_PATH, bug.benchmark.name, bug.project, str(bug.bug_id), self.name,
                                       str(self.seed), "result.json"), "w+") as fd2:
                    json.dump(result, fd2, indent=2)
                if len(result['patches']) > 0:
                    repair_task.status = "PATCHED"
            cmd = "rm -rf %s;" % (bug_path)
            subprocess.call(cmd, shell=True)

    pass
