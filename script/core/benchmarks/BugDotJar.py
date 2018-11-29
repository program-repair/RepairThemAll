import os
import shutil
import subprocess
import json
import re
from sets import Set

from config import REPAIR_ROOT
from core.Benchmark import Benchmark
from core.Bug import Bug


FNULL = open(os.devnull, 'w')

class BugDotJar(Benchmark):
    """Bug_dot_jar Benchmark"""

    def __init__(self):
        super(BugDotJar, self).__init__("Bug_dot_jar")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "Bug-dot-jar")
        self.bugs = None
        self.get_bugs()

    def get_bug(self, bug_id):
        separator = "-"
        if "_" in bug_id:
            separator = "_"
        split = bug_id.split(separator)
        commit = split[-1]
        project = "-".join(split[:-1])
        for bug in self.get_bugs():
            if project.lower() in bug.project.lower():
                if bug.bug_id[:8].lower() == commit[:8]:
                    return bug
        return None

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs
        self.bugs = []
        dataset_path = os.path.join(self.path, "data")
        for project in os.listdir(dataset_path):
            project_path = os.path.join(dataset_path, project)
            if os.path.isfile(project_path):
                continue
            for commit in os.listdir(project_path):
                commit_path = os.path.join(project_path, commit)
                if not os.path.isfile(commit_path) or commit[-5:] != ".json":
                    continue
                bug = Bug(self, project.title(), commit[:-5])
                self.bugs += [bug]
        return self.bugs

    def checkout(self, bug, working_directory):
        dataset_path = os.path.join(self.path, "data", bug.project.lower(), "%s.json" % bug.bug_id[:8])
        with open(dataset_path) as fd:
            data = json.load(fd)
            project = bug.project.split("-")[-1].upper()
            branch_id = "bugs-dot-jar_%s-%s_%s" % (project, data['jira_id'], data['commit'])
            cmd = "cd " + os.path.join(self.path, "repositories", bug.project.lower()) + "; git reset .; git checkout -- .; git clean -x -d --force; git checkout master; git checkout " + branch_id
            subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
            shutil.copytree(os.path.join(self.path, "repositories", bug.project.lower()), working_directory)
        pass

    def compile(self, bug, working_directory):
        cmd = """cd %s;
        mvn install -V -B -DskipTests -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true; 
        mvn test -DskipTests -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true;
        mvn dependency:build-classpath -Dmdep.outputFile="classpath.info";
        """ % (working_directory)
        subprocess.call(cmd, shell=True)
        pass

    def run_test(self, bug, working_directory):
        cmd = "cd %s; mvn test;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def failing_tests(self, bug):
        tests = []
        maven_output = os.path.join(bug.working_directory, ".bugs-dot-jar", "test-results.txt")
        with open(maven_output) as fd:
            content = fd.read()
            matches = re.findall("<<< FAILURE! - in (.*)", content)
            for m in matches:
                tests.append(m)
            matches = re.findall("\((.+)\) .+ <<< FAILURE!", content)
            for m in matches:
                tests.append(m)
        return tests

    def source_folders(self, bug):
        folders = []
        for (root, dirnames, _) in os.walk(bug.working_directory):
            for d in dirnames:
                if d == "src" or d == "source":
                    if os.path.exists(os.path.join(root, d, "main")):
                        if os.path.exists(os.path.join(root, d, "java")):
                            folders += [os.path.join(root, d, "java")]
                        else:
                            folders += [os.path.join(root, d, "main")]
                    else:
                        folders += [os.path.join(root, d)]
        return folders

    def test_folders(self, bug):
        folders = []

        for (root, dirnames, _) in os.walk(bug.working_directory):
            for d in dirnames:
                if d == "test":
                    folders += [os.path.join(root, d)]
        return folders

    def bin_folders(self, bug):
        folders = []
        for (root, dirnames, _) in os.walk(bug.working_directory):
            for d in dirnames:
                if d == "target":
                    if os.path.exists(os.path.join(root, d, "classes")):
                        folders += [os.path.join(root, d, "classes")]
        return folders

    def test_bin_folders(self, bug):
        folders = []
        for (root, dirnames, _) in os.walk(bug.working_directory):
            for d in dirnames:
                if d == "target":
                    if os.path.exists(os.path.join(root, d, "test-classes")):
                        folders += [os.path.join(root, d, "test-classes")]
        return folders

    def classpath(self, repair_task):
        classpath = ""
        workdir = repair_task.working_directory

        m2_repository = os.path.expanduser("~/.m2/repository")

        dependencies = Set()
        for (root, _, files) in os.walk(workdir):
            for f in files:
                if f == "classpath.info":
                    with open(os.path.join(root, f)) as fd:
                        classpath_info = fd.read()
                        for lib in classpath_info.split(":"):
                            if ".m2" not in lib:
                                continue
                            lib = lib[lib.index(".m2") + 4:].replace("repository/", "")
                            tmp = lib.split("/")
                            jar = tmp[-1]
                            version = tmp[-2]
                            artifact_id = tmp[-3]
                            group_id = ".".join(tmp[:-3])

                            dependencies.add(os.path.join(m2_repository, group_id.replace(".", "/"), artifact_id,
                                                          version, jar))

        for dep in dependencies:
            if os.path.exists(dep):
                if classpath != "":
                    classpath += ":"
                classpath += dep
            else:
                print("[Error] Dep %s is not found" % (path.replace(m2_repository, "")))
        return classpath

    def compliance_level(self, bug):
        return 7
