import os
import json
import subprocess

from config import REPAIR_ROOT, DATA_PATH

from core.Benchmark import Benchmark
from core.Bug import Bug


class Bears(Benchmark):
    """Bears Benchmark"""

    def __init__(self):
        super(Bears, self).__init__("Bears")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "bears")
        self.project_data = {}
        self.bugs = None
        self.get_bugs()

    def get_bug(self, bug_id):
        separator = "-"
        splitted = bug_id.split(separator)
        patched = splitted[-1]
        buggy = splitted[-2]
        project = "-".join(splitted[:-2])
        return Bug(self, project, "%s-%s" % (buggy, patched))

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
                self.bugs += [Bug(self, "%s-%s" % (organization, project), "%s_%s" % (b['builds']['buggyBuild'], b['builds']['fixerBuild']))]
        return self.bugs

    def checkout(self, bug, working_directory):
        branch_id = "%s-%s" % (bug.project, bug.bug_id)

        cmd = "cd " + self.path + "; git checkout " + branch_id
        subprocess.check_output(cmd, shell=True)

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
        subprocess.call(cmd, shell=True)
        pass

    def compile(self, bug, working_directory):
        cmd = """cd %s;
mvn compile;
""" % (working_directory)
        subprocess.call(cmd, shell=True)
        pass

    def run_test(self, bug, working_directory):
        cmd = """cd %s;
mvn package -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true
""" % (working_directory)
        subprocess.call(cmd, shell=True)
        pass

    def failing_tests(self, bug):
        tests = []
        with open(os.path.join(self.get_data_path(), "bugs.json")) as fd:
            data = json.load(fd)
            for b in data:
                (organization, project) = b["repository"]["url"].replace("https://github.com/", "").split("/")
                project_id = "%s-%s" % (organization, project)
                bug_id = "%s_%s" % (b['builds']['buggyBuild'], b['builds']['fixerBuild'])

                if bug.project == project_id and bug.bug_id == bug_id:
                    for t in b['tests']['failingClasses']:
                        tests += [t['testClass']]
                    return tests
        return tests

    def source_folders(self, bug):
        # TODO
        return []

    def test_folders(self, bug):
        # TODO
        return []

    def bin_folders(self, bug):
        # TODO
        return []

    def test_bin_folders(self, bug):
        # TODO
        return []

    def classpath(self, bug):
        classpath = ""
        return classpath

    def compliance_level(self, bug):
        return 8
