import os
import shutil
import subprocess

from config import REPAIR_ROOT
from core.Benchmark import Benchmark
from core.Bug import Bug
from core.utils import add_benchmark

FNULL = open(os.devnull, 'w')

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
                    if revision == "reference":
                        continue
                    revision_path = os.path.join(user_path, revision)
                    if os.path.isfile(revision_path):
                        continue
                    bug = Bug(self, project, "%s_%s" % (user, revision))
                    self.bugs += [bug]
        return self.bugs

    def get_bug(self, bug_id):
        separator = "-"
        if "_" in bug_id:
            separator = "_"
        elif "/" in bug_id:
            separator = "/"
        (project, user, revision) = bug_id.split(separator)

        for bug in self.get_bugs():
            if project != bug.project:
                continue
            (bug_user, bug_revision) = bug.bug_id.split("_")
            if user in bug_user and int(revision) == int(bug_revision):
                return bug
        return None

    def checkout(self, bug, working_directory):
        user, revision = bug.bug_id.split("_")
        bug_path = os.path.join(self.path, "dataset", bug.project, user, revision)
        shutil.copytree(bug_path, working_directory)
        pass

    def compile(self, bug, working_directory):
        cmd = "cd %s; export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true; mvn test -DskipTests;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def run_test(self, bug, working_directory):
        cmd = "cd %s; export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true; mvn test;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def failing_tests(self, bug):
        (bug_user, bug_revision) = bug.bug_id.split("_")
        bug_user = bug_user[:8]
        tests = [
            "introclassJava.%s_%s_%sBlackboxTest" % (bug.project.lower(), bug_user, bug_revision),
            "introclassJava.%s_%s_%sWhiteboxTest" % (bug.project.lower(), bug_user, bug_revision)
        ]

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
        classpath = []
        m2_repository = os.path.expanduser("~/.m2/repository")
        classpath.append(os.path.join(m2_repository, "junit", "junit", "4.11", "junit-4.11.jar"))
        classpath.append(os.path.join(m2_repository, "org", "hamcrest", "hamcrest-core", "1.3", "hamcrest-core-1.3.jar"))
        return ":".join(classpath)

    def compliance_level(self, bug):
        return 7

add_benchmark("IntroClassJava", IntroClassJava)