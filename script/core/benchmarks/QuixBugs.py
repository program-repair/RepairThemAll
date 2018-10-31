import os
import shutil
import subprocess

from config import REPAIR_ROOT
from core.Benchmark import Benchmark
from core.Bug import Bug


class QuixBugs(Benchmark):
    """QuixBugs Benchmark"""

    def __init__(self):
        super(QuixBugs, self).__init__("QuixBugs")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "QuixBugs")
        self.bugs = None
        self.get_bugs()

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs
        self.bugs = []
        dataset_path = os.path.join(self.path, "java_programs")
        for program in os.listdir(dataset_path):
            project_path = os.path.join(dataset_path, program)
            if not os.path.isfile(project_path) or ".class" in program:
                continue

            bug = Bug(self, program.replace(".java", ""), "")
            self.bugs += [bug]
        return self.bugs

    def checkout(self, bug, working_directory):
        dataset_path = os.path.join(self.path, "java_programs")
        # TODO create folders
        # TODO copy src, test and QuixFixOracleHelper
        bug_path = ""
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

    def classpath(self, bug):
        return ":".join(self.bin_folders(bug) + self.test_bin_folders(bug))

    def compliance_level(self, bug):
        return 7
