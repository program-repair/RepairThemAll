import json
import os
import subprocess

from config import REPAIR_ROOT, DATA_PATH
from core.Benchmark import Benchmark
from core.Bug import Bug

FNULL = open(os.devnull, 'w')


class Bears(Benchmark):
    """Bears Benchmark"""

    def __init__(self):
        super(Bears, self).__init__("Bears")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "bears")
        self.project_data = {}
        self.bugs = None
        self.get_bugs()
        self.sources = None
        with open(os.path.join(self.get_data_path(), "sources.json")) as fd:
            self.sources = json.load(fd)

    def get_bug(self, bug_id):
        bug_id = bug_id.replace("_", "-")
        separator = "-"
        splitted = bug_id.split(separator)
        patched = splitted[-1]
        buggy = splitted[-2]
        project = "-".join(splitted[:-2])

        for bug in self.get_bugs():
            if bug.project.lower() == project.lower():
                if bug.bug_id.lower() == ("%s-%s" % (buggy, patched)):
                    return bug
        return None

    def get_data_path(self):
        return os.path.join(DATA_PATH, "benchmarks", "bears")

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs

        self.bugs = []
        with open(os.path.join(self.get_data_path(), "bugs.json")) as fd:
            data = json.load(fd)
            for b in data:
                (organization, project) = b["repository"]["url"].replace("https://github.com/", "").split("/")
                self.bugs += [Bug(self, "%s-%s" % (organization, project),
                                  "%s-%s" % (b['builds']['buggyBuild']['id'], b['builds']['fixerBuild']['id']))]
        return self.bugs

    def checkout(self, bug, working_directory):
        branch_id = "%s-%s" % (bug.project, bug.bug_id)

        cmd = "cd " + self.path + "; git reset .; git checkout -- .; git clean -x -d --force; git checkout master; git checkout " + branch_id
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

        cmd = "cd " + self.path + "; git log --format=format:%H --grep='Changes in the tests'"
        bug_commit = subprocess.check_output(cmd, shell=True)
        if len(bug_commit) == 0:
            cmd = "cd " + self.path + "; git log --format=format:%H --grep='Bug commit'"
            bug_commit = subprocess.check_output(cmd, shell=True)

        cmd = """cd %s;
git checkout %s;
cp -r . %s""" % (
            self.path,
            bug_commit,
            working_directory,
        )
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def compile(self, bug, working_directory):
        cmd = """cd %s;
mvn install -V -B -DskipTests -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true; 
mvn test -DskipTests -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true;
mvn dependency:build-classpath -Dmdep.outputFile="classpath.info";
""" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def run_test(self, bug, working_directory):
        cmd = """cd %s;
mvn package -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true
""" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def failing_tests(self, bug):
        tests = []
        with open(os.path.join(self.get_data_path(), "bugs.json")) as fd:
            data = json.load(fd)
            for b in data:
                (organization, project) = b["repository"]["url"].replace("https://github.com/", "").split("/")
                project_id = "%s-%s" % (organization, project)
                bug_id = "%s-%s" % (b['builds']['buggyBuild']['id'], b['builds']['fixerBuild']['id'])

                if bug.project.lower() == project_id.lower() and bug.bug_id.lower() == bug_id.lower():
                    for t in b['tests']['failingClasses']:
                        tests += [t['testClass']]
                        return tests
        return tests

    def source_folders(self, bug):
        folders = []
        branch_id = "%s-%s" % (bug.project, bug.bug_id)

        if bug.project.lower() in self.sources:
            return self.sources[bug.project.lower()]['sources']

        cmd = "cd " + self.path + "; git checkout " + branch_id
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        for (root, dirnames, _) in os.walk(self.path):
            path_project = root.replace(self.path, "")
            if len(path_project) > 0 and path_project[0] == "/":
                path_project = path_project[1:]
            for d in dirnames:
                if d == "src" or d == "source":
                    if os.path.exists(os.path.join(root, d, "main")):
                        if os.path.exists(os.path.join(root, d, "java")):
                            folders += [os.path.join(path_project, d, "java")]
                        else:
                            folders += [os.path.join(path_project, d, "main")]
                    else:
                        folders += [os.path.join(path_project, d)]
        return folders

    def test_folders(self, bug):
        if bug.project.lower() in self.sources:
            return self.sources[bug.project.lower()]['tests']

        folders = []
        branch_id = "%s-%s" % (bug.project, bug.bug_id)

        cmd = "cd " + self.path + "; git checkout " + branch_id
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        for (root, dirnames, _) in os.walk(self.path):
            path_project = root.replace(self.path, "")
            if len(path_project) > 0 and path_project[0] == "/":
                path_project = path_project[1:]
            for d in dirnames:
                if d == "test":
                    folders += [os.path.join(path_project, d)]
        return folders

    def bin_folders(self, bug):
        if bug.project.lower() in self.sources:
            return self.sources[bug.project.lower()]['source-target']
        # TODO
        return ["target/classes"]

    def test_bin_folders(self, bug):
        if bug.project.lower() in self.sources:
            return self.sources[bug.project.lower()]['test-target']
        # TODO
        return ["target/test-classes"]

    def classpath(self, repair_task):
        classpath = ""
        workdir = repair_task.working_directory

        m2_repository = os.path.expanduser("~/.m2/repository")

        dependencies = []
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

                            dependencies += [{
                                "group_id": group_id,
                                "artifact_id": artifact_id,
                                "version": version,
                                "jar": jar
                            }]

        for dep in dependencies:
            path = os.path.join(m2_repository, dep['group_id'].replace(".", "/"), dep['artifact_id'],
                                dep['version'], dep['jar'])
            if os.path.exists(path):
                if classpath != "":
                    classpath += ":"
                classpath += path
            else:
                print("[Error] Dep %s is not found" % (path.replace(m2_repository, "")))
        return classpath

    def compliance_level(self, bug):
        return 8
