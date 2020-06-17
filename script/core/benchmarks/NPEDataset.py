import os
import shutil
import subprocess
import json

from config import REPAIR_ROOT
from core.Benchmark import Benchmark
from core.Bug import Bug
from core.utils import add_benchmark

FNULL = open(os.devnull, 'w')

class NPEDataset(Benchmark):
    """NPEDataset Benchmark"""

    def __init__(self):
        super(NPEDataset, self).__init__("NPEDataset")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "npe-dataset")
        self.bug_names = ["collections-360", "felix-4960", "lang304", "lang-587", "lang-703", "math-290", "math-305", "math-369", "math-988a", "math-988b", "math-1115", "math-1117", "pdfbox_2812", "pdfbox_2965", "pdfbox_2995", "sling_4982"]
        self.bugs = None
        self.get_bugs()

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs
        self.bugs = []
        for bug in self.bug_names:
            bug = Bug(self, bug, "")
            self.bugs += [bug]    
        return self.bugs

    def get_bug(self, bug_id):
        if bug_id[-1] == '_':
            bug_id = bug_id[:-1]
        for bug in self.get_bugs():
            if bug_id.lower() == bug.project.lower():
                return bug
        return None

    def checkout(self, bug, working_directory, buggy_version=True):
        bug_path = os.path.join(self.path, bug.project)
        shutil.copytree(bug_path, working_directory)
        pass

    def compile(self, bug, working_directory):
        cmd = "cd %s; export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true; mvn -Dhttps.protocols=TLSv1.2 test -DskipTests;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def run_test(self, bug, working_directory, test=None):
        cmd = "cd %s; export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true; mvn -Dhttps.protocols=TLSv1.2 test;" % (working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def _get_project_info(self, bug):
        try:
            return bug.maven_info
        except AttributeError:
            pass        
        cmd = """cd %s;
mvn com.github.tdurieux:project-config-maven-plugin:1.0-SNAPSHOT:info -q;
""" % (bug.working_directory)
        info = json.loads(subprocess.check_output(cmd, shell=True))
        bug.maven_info = info
        return info

    def failing_tests(self, bug):
        tests = []
        return tests

    def source_folders(self, bug):
        bug_path = os.path.join(self.path, bug.project)
        if os.path.exists(os.path.join(bug_path, "src", 'main')):
            if os.path.exists(os.path.join(bug_path, "src", 'main', 'java')):
                return [os.path.join("src", "main", "java")]
            return [os.path.join("src", "main")]
        elif os.path.exists(os.path.join(bug_path, "src", 'java')):
            return [os.path.join("src", "java")]
        return [os.path.join("src")]

    def test_folders(self, bug):
        bug_path = os.path.join(self.path, bug.project)
        if os.path.exists(os.path.join(bug_path, "src", 'test')):
            if os.path.exists(os.path.join(bug_path, "src", 'test', 'java')):
                return [os.path.join("src", "test", "java")]
            return [os.path.join("src", "test")]
        elif os.path.exists(os.path.join(bug_path, "test", 'java')):
            return [os.path.join("test", "java")]
        return [os.path.join("test")]

    def bin_folders(self, bug):
        return [os.path.join("target", "classes")]

    def test_bin_folders(self, bug):
        return [os.path.join("target", "test-classes")]

    def classpath(self, bug):
        info = self._get_project_info(bug)
        return ":".join(info['classpath'])

    def compliance_level(self, bug):
        info = self._get_project_info(bug)
        return info['complianceLevel']

add_benchmark("NPEDataset", NPEDataset)