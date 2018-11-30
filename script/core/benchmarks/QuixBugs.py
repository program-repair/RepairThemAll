import os
import shutil
import subprocess

from config import REPAIR_ROOT, DATA_PATH
from core.Benchmark import Benchmark
from core.Bug import Bug

FNULL = open(os.devnull, 'w')


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
            program = program.replace(".java", "")
            if not os.path.isfile(project_path) or program != program.upper():
                continue
            bug = Bug(self, program, "")
            self.bugs += [bug]
        return self.bugs

    def get_bug(self, bug_id):
        for bug in self.get_bugs():
            if bug_id.lower() == bug.project.lower():
                return bug
        return None

    def checkout(self, bug, working_directory):
        dataset_path = os.path.join(self.path, "java_programs")
        test_path = os.path.join(self.path, "java_testcases", "junit")

        source_path = os.path.join(working_directory, "src", "main", "java")
        test_dst_path = os.path.join(working_directory, "src", "test", "java")

        os.makedirs(test_dst_path)
        os.makedirs(source_path)

        shutil.copy(os.path.join(DATA_PATH, "benchmarks", "QuixBugs", "pom.xml"), working_directory)
        for program in os.listdir(dataset_path):
            project_path = os.path.join(dataset_path, program)
            program = program.replace(".java", "")
            if not os.path.isfile(project_path) or ".class" in program or program == program.upper():
                continue
            shutil.copy(project_path, source_path)

        shutil.copy(os.path.join(dataset_path, "%s.java" % bug.project), source_path)
        test_file_path = os.path.join(test_path, "%s_TEST.java" % bug.project)
        if os.path.exists(test_file_path):
            self.prepare_test(bug, test_dst_path, test_file_path)
        else:
            test_file_path = os.path.join(DATA_PATH, "benchmarks", "QuixBugs", "%s_TEST.java" % bug.project)
            if os.path.exists(test_file_path):
                self.prepare_test(bug, test_dst_path, test_file_path)
        shutil.copy(os.path.join(test_path, "QuixFixOracleHelper.java"), test_dst_path)


        # TODO create folders
        # TODO copy src, test and QuixFixOracleHelper
        pass

    def prepare_test(self, bug, test_dst_path, test_file_path):
        with open(test_file_path) as fd1:
            content = fd1.read().replace("%s_TEST" % bug.project, "%s_Test" % bug.project)
            with open(os.path.join(test_dst_path, "%s_Test.java" % bug.project), "w+") as fd2:
                fd2.write(content)

    def compile(self, bug, working_directory):
        cmd = "cd %s; mvn test -DskipTests;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def run_test(self, bug, working_directory):
        cmd = "cd %s; mvn test;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def failing_tests(self, bug):
        tests = ["java_testcases.junit.%s_Test" % bug.project]
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
        classpath = []
        m2_repository = os.path.expanduser("~/.m2/repository")
        classpath.append(os.path.join(m2_repository, "junit", "junit", "4.11", "junit-4.11.jar"))
        classpath.append(
            os.path.join(m2_repository, "org", "hamcrest", "hamcrest-core", "1.3", "hamcrest-core-1.3.jar"))
        return ":".join(classpath)

    def compliance_level(self, bug):
        return 8
