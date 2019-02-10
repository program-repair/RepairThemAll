import collections
import json
import os
import re
import subprocess
from sets import Set

from config import DATA_PATH
from config import REPAIR_ROOT
from core.Benchmark import Benchmark
from core.Bug import Bug
from core.utils import add_benchmark

FNULL = open(os.devnull, 'w')


class Defects4J(Benchmark):
    """Defects4j Benchmark"""

    def __init__(self):
        super(Defects4J, self).__init__("Defects4J")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "defects4j")
        self.project_data = {}
        self.bugs = None
        self.get_bugs()

    def get_data_path(self):
        return os.path.join(DATA_PATH, "benchmarks", "defects4j")

    def get_bug(self, bug_id):
        separator = "-"
        if "_" in bug_id:
            separator = "_"
        (project, id) = bug_id.split(separator)
        for bug in self.get_bugs():
            if bug.project.lower() == project.lower():
                if int(bug.bug_id) == int(id):
                    return bug
        return None

    def get_bugs(self):
        if self.bugs is not None:
            return self.bugs
        self.bugs = []
        data_defects4j_path = self.get_data_path()
        for project_data in os.listdir(data_defects4j_path):
            project_data_path = os.path.join(data_defects4j_path, project_data)
            if not os.path.isfile(project_data_path):
                continue
            with open(project_data_path) as fd:
                data = json.load(fd)
                self.project_data[data['project']] = data
                for i in range(1, data['nbBugs'] + 1):
                    bug = Bug(self, data['project'], i)
                    bug.project_data = data
                    self.bugs += [bug]
        return self.bugs

    def _get_benchmark_path(self):
        return os.path.join(self.path, "framework", "bin")

    def checkout(self, bug, working_directory):
        print bug, working_directory
        cmd = """export PATH="%s:$PATH";
defects4j checkout -p %s -v %sb -w %s;
""" % (self._get_benchmark_path(),
       bug.project,
       bug.bug_id,
       working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def compile(self, bug, working_directory):
        cmd = """export PATH="%s:$PATH";
cd %s;
defects4j compile;
""" % (self._get_benchmark_path(),
       working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def run_test(self, bug, working_directory):
        cmd = """export PATH="%s:$PATH";
cd %s;
defects4j test;
""" % (self._get_benchmark_path(),
       working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def failing_tests(self, bug):
        cmd = """export PATH="%s:$PATH";
defects4j info -p %s -b %s;
""" % (self._get_benchmark_path(), bug.project, bug.bug_id)
        info = subprocess.check_output(cmd, shell=True)

        tests = Set()
        reg = re.compile('- (.*)::(.*)')
        m = reg.findall(info)
        for i in m:
            tests.add(i[0])
        return list(tests)

    def source_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(sorted(sources.items(), key=lambda t: int(t[0])))

        source = None
        for index, src in sources.iteritems():
            if bug.bug_id <= int(index):
                source = src['srcjava']
                break
        return [source]

    def test_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(sorted(sources.items(), key=lambda t: int(t[0])))

        source = None
        for index, src in sources.iteritems():
            if bug.bug_id <= int(index):
                source = src['srctest']
                break
        return [source]

    def bin_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(sorted(sources.items(), key=lambda t: int(t[0])))
        source = None
        for index, src in sources.iteritems():
            if bug.bug_id <= int(index):
                source = src['binjava']
                break
        return [source]

    def test_bin_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(sorted(sources.items(), key=lambda t: int(t[0])))

        source = None
        for index, src in sources.iteritems():
            if bug.bug_id <= int(index):
                source = src['bintest']
                break
        return [source]

    def classpath(self, repair_task):
        bug = repair_task.bug
        classpath = ""
        workdir = repair_task.working_directory

        sources = self.project_data[bug.project]["classpath"]
        sources = collections.OrderedDict(sorted(sources.items(), key=lambda t: int(t[0])))
        for index, cp in sources.iteritems():
            if bug.bug_id <= int(index):
                for c in cp.split(":"):
                    if classpath != "":
                        classpath += ":"
                    classpath += os.path.join(workdir, c)
                break
        for (root, _, files) in os.walk(os.path.join(workdir, "lib")):
            for f in files:
                if f[-4:] == ".jar":
                    classpath += ":" + (os.path.join(root, f))
        libs = []
        cmd = """export PATH="%s:$PATH";
        cd %s;
        defects4j export -p cp.test 2> /dev/null;
        """ % (self._get_benchmark_path(), repair_task.working_directory)
        libs_split = subprocess.check_output(cmd, shell=True).split(":")
        for lib_str in libs_split:
            lib = os.path.basename(lib_str)
            if lib[-4:] == ".jar":
                libs.append(lib)
        libs_path = os.path.join(self.path, "framework", "projects", bug.project, "lib")
        for (root, _, files) in os.walk(libs_path):
            for f in files:
                if f in libs:
                    classpath += ":" + (os.path.join(root, f))
        libs_path = os.path.join(self.path, "framework", "projects", "lib")
        for (root, _, files) in os.walk(libs_path):
            for f in files:
                if f in libs:
                    classpath += ":" + (os.path.join(root, f))

        return classpath


    def compliance_level(self, bug):
        return self.project_data[bug.project]["complianceLevel"][str(bug.bug_id)]["source"]

add_benchmark("Defects4J", Defects4J)