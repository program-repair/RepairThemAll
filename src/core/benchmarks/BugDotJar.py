import os
import shutil
import subprocess
import json
# from sets import Set

from config import REPAIR_ROOT, JAVA7_HOME, JAVA8_HOME, MAVEN_BIN
from core.Benchmark import Benchmark
from core.Bug import Bug
from core.utils import add_benchmark

FNULL = open(os.devnull, 'w')


def abs_to_rel(root, folders):
    if root[-1] != '/':
        root += "/"
    output = []
    for folder in folders:
        output.append(folder.replace(root, ""))
    return output


class BugDotJar(Benchmark):
    """Bug_dot_jar Benchmark"""

    def __init__(self):
        super(BugDotJar, self).__init__("Bugs.jar")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "bugs-dot-jar")
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

    def checkout(self, bug, working_directory, buggy_version=True):
        dataset_path = os.path.join(
            self.path, "data", bug.project.lower(), "%s.json" % bug.bug_id[:8])
        with open(dataset_path) as fd:
            data = json.load(fd)
            project = bug.project.split("-")[-1].upper()
            commit = data['commit']
            if buggy_version == False:
                commit = data['commit']
            branch_id = "bugs-dot-jar_%s-%s_%s" % (
                project, data['jira_id'], commit)
            cmd = "cd " + os.path.join(self.path, "repositories",
                                       bug.project.lower()) + "; git reset .; git checkout -- .; git clean -x -d --force; git checkout master; git checkout " + branch_id
            print('BugDotJar checkout cmd: ', cmd)
            subprocess.call(cmd, shell=True, stdout=FNULL,
                            stderr=subprocess.STDOUT)
            shutil.copytree(os.path.join(self.path, "repositories",
                            bug.project.lower()), working_directory)
        pass

    def compile(self, bug, working_directory):
        java_version = os.path.join(JAVA8_HOME, '..')
        if bug.project == "Wicket":
            java_version = os.path.join(JAVA7_HOME, '..')
        cmd = """cd %s;
        export JAVA_HOME="%s";
        export PATH="%s:$PATH";
        export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true;
        mvn -Dhttps.protocols=TLSv1.2 install -V -B -DskipTests -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true; 
        mvn -Dhttps.protocols=TLSv1.2 test -DskipTests -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true -Dhttps.protocols=TLSv1.2;
        mvn dependency:build-classpath -Dmdep.outputFile="classpath.info";
        """ % (working_directory, java_version, MAVEN_BIN)
        out = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT)
        return out.decode("utf-8")

    def run_test(self, bug, working_directory, test=None):
        java_version = os.path.join(JAVA8_HOME, '..')
        if bug.project == "Wicket":
            java_version = os.path.join(JAVA7_HOME, '..')
        cmd = """cd %s; 
        export JAVA_HOME="%s";
        export PATH="%s:$PATH";
        export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true;
        rm -rf .git; git init; git commit -m 'init' --allow-empty;
        mvn -Dhttps.protocols=TLSv1.2 test -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true -Djacoco.skip=true -Dhttps.protocols=TLSv1.2;""" % (working_directory, java_version, MAVEN_BIN)

        print('BugDotJar run_test cmd: ', cmd)
        out = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT)
        print('running on working_directory: ', working_directory)
        testing_output = out.decode("utf-8")
        print('testing_output: ', testing_output)
        return self.get_maven_test_results(bug, working_directory)

    def failing_module(self, bug):
        info = self._get_project_info(bug)
        failing_tests = self.failing_tests(bug)
        path_failing_test = failing_tests[0].replace(".", "/") + ".java"

        for module in info['modules']:
            module_name = os.path.basename(module['baseDir'])
            for test_folder in module['tests']:
                if os.path.exists(os.path.join(test_folder, path_failing_test)):
                    return module_name
        return "root"

    def failing_tests(self, bug):
        dataset_path = os.path.join(
            self.path, "data", bug.project.lower(), "%s.json" % bug.bug_id[:8])
        with open(dataset_path) as fd:
            data = json.load(fd)
            return data['failing_tests']

    def source_folders(self, bug):
        folders = []

        info = self._get_project_info(bug)
        failing_module = self.failing_module(bug)

        for module in info['modules']:
            module_name = os.path.basename(module['baseDir'])
            if failing_module == module_name or failing_module == module['name']:
                return abs_to_rel(bug.working_directory, module['sources'])
        return folders

    def test_folders(self, bug):
        folders = []

        info = self._get_project_info(bug)
        failing_module = self.failing_module(bug)

        for module in info['modules']:
            module_name = os.path.basename(module['baseDir'])
            if failing_module == module_name or failing_module == module['name']:
                return abs_to_rel(bug.working_directory, module['tests'])

        return folders

    def bin_folders(self, bug):
        info = self._get_project_info(bug)
        failing_module = self.failing_module(bug)

        for module in info['modules']:
            module_name = os.path.basename(module['baseDir'])
            if failing_module == module_name or failing_module == module['name']:
                return abs_to_rel(bug.working_directory, module['binSources'])
        return []

    def test_bin_folders(self, bug):
        info = self._get_project_info(bug)
        failing_module = self.failing_module(bug)

        for module in info['modules']:
            module_name = os.path.basename(module['baseDir'])
            if failing_module == module_name or failing_module == module['name']:
                return abs_to_rel(bug.working_directory, module['binTests'])
        return []

    def classpath(self, bug):
        info = self._get_project_info(bug)
        failing_module = self.failing_module(bug)

        deps = []

        for module in info['modules']:
            module_name = os.path.basename(module['baseDir'])
            if failing_module != module_name and failing_module != module['name']:
                deps += module['binSources']
        deps += info['classpath']

        return ":".join(deps)

    def compliance_level(self, bug):
        return 7


add_benchmark("Bugs.jar", BugDotJar)
