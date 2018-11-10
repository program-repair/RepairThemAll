import os
import shutil
import subprocess

from config import REPAIR_ROOT
from core.Benchmark import Benchmark
from core.Bug import Bug


class IntroClassJava(Benchmark):
    """IntroClassJava Benchmark"""

    def __init__(self):
        super(IntroClassJava, self).__init__("IntroClassJava")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "IntroclassJava")
        self.bugs = None
        self.get_bugs()

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs
        self.bugs = []
        dataset_path = os.path.join(self.path, "dataset")
        for project in os.listdir(dataset_path):
            project_path = os.path.join(dataset_path, project)
            if os.path.isfile(project_path):
                continue
            for user in os.listdir(project_path):
                user_path = os.path.join(project_path, user)
                if os.path.isfile(user_path):
                    continue
                for revision in os.listdir(user_path):
                    revision_path = os.path.join(user_path, revision)
                    if os.path.isfile(revision_path):
                        continue
                    bug = Bug(self, project, "%s_%s" % (user, revision))
                    self.bugs += [bug]
        return self.bugs

    def checkout(self, bug, working_directory):
        user, revison = bug.bug_id.split("_")
        bug_path = os.path.join(self.path, "dataset", bug.project, user, revision)
        shutil.copy(bug_path, working_directory)
        pass

    def compile(self, bug, working_directory):
        cmd = "cd %s; mvn test -Dmaven.test.skip=true;" % (working_directory)
        subprocess.call(cmd, shell=True)
        pass

    def run_test(self, bug, working_directory):
        cmd = "cd %s; mvn test;" % (working_directory)
        subprocess.call(cmd, shell=True)
        pass

    def failing_tests(self, bug):
        tests = []
        return tests

    def source_folders(self, bug):
        return [os.path.join("src", "main", "java")]

    def test_folders(self, bug):
        return [os.path.join("src", "test", "java")]

    def bin_folders(self, bug):
        return [os.path.join("target", "classes")]

    def test_bin_folders(self, bug):
        return [os.path.join("target", "test-classes")]

    def classpath(self, repair_task):
        return ""

    def compliance_level(self, bug):
        return 7
