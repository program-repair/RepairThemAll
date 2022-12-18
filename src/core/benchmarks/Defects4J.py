import collections
import json
import os
import re
import subprocess
# from sets import Set

from config import DATA_PATH, JAVA8_HOME, JAVA8_HOME
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

    def checkout(self, bug, working_directory, buggy_version=True):
        print('Defects4J checkout...')
        print('bug:', bug)
        if buggy_version:
            version = 'b'
            print('checking out buggy version')
        else:
            version = 'f'
            print('checking out fixed version')

        cmd = """export PATH="%s:%s:$PATH";export JAVA_HOME="%s";
defects4j checkout -p %s -v %s%s -w %s;
""" % (JAVA8_HOME,
            self._get_benchmark_path(),
            os.path.join(JAVA8_HOME, '..'),
            bug.project,
            bug.bug_id,
            version,
            working_directory)
        print('Defects4J checkout cmd: ', cmd)
        subprocess.call(cmd, shell=True)
        pass

    def compile(self, bug, working_directory):
        print('Defects4J compile...')
        cmd = """export PATH="%s:%s:$PATH";export JAVA_HOME="%s";
export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true;
cd %s;
defects4j compile;
""" % (JAVA8_HOME,
            self._get_benchmark_path(),
            os.path.join(JAVA8_HOME, '..'),
            working_directory)
        subprocess.call(cmd, shell=True)
        pass

    def run_test(self, bug, working_directory, test=None):
        print('Defects4J running test...')
        test_arg = ""
        if test is not None:
            test_arg = "-t %s" % (test)
        cmd = """export PATH="%s:%s:$PATH";export JAVA_HOME="%s";
export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true; 
cd %s;
defects4j test %s;
""" % (JAVA8_HOME,
            self._get_benchmark_path(),
            os.path.join(JAVA8_HOME, '..'),
            working_directory,
            test_arg)
        subprocess.check_call(cmd, shell=True)
        if os.path.exists(os.path.join(working_directory, "failing_tests")):
            with open(os.path.join(working_directory, "failing_tests")) as fd:
                return fd.read()
        pass

    def failing_tests(self, bug):
        cmd = """export PATH="%s:%s:$PATH";export JAVA_HOME="%s";
export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true;
defects4j info -p %s -b %s;
""" % (JAVA8_HOME,
            self._get_benchmark_path(),
            os.path.join(JAVA8_HOME, '..'),
            bug.project,
            bug.bug_id)
        try:
            # info = subprocess.check_output(cmd, shell=True, stderr=FNULL)
            info = subprocess.check_output(
                'defects4j info -p Closure -b 18;', shell=True, stderr=FNULL)
            tests = set()
            reg = re.compile('- (.*)::(.*)')
            m = reg.findall(str(info, 'utf-8'))
            for i in m:
                tests.add(i[0])
            return list(tests)
        except subprocess.CalledProcessError as e:
            print('----------ERROR------------')
            print(e.output)
            print('----------cmd--------------')
            print(cmd)
            print('----------end--------------')

    def source_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(
            sorted(sources.items(), key=lambda t: int(t[0])))

        source = None
        for index, src in sources.items():
            if bug.bug_id <= int(index):
                source = src['srcjava']
                break
        return [source]

    def test_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(
            sorted(sources.items(), key=lambda t: int(t[0])))

        source = None
        for index, src in sources.items():
            if bug.bug_id <= int(index):
                source = src['srctest']
                break
        return [source]

    def bin_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(
            sorted(sources.items(), key=lambda t: int(t[0])))
        source = None
        for index, src in sources.items():
            if bug.bug_id <= int(index):
                source = src['binjava']
                break
        return [source]

    def test_bin_folders(self, bug):
        sources = self.project_data[bug.project]["src"]
        sources = collections.OrderedDict(
            sorted(sources.items(), key=lambda t: int(t[0])))

        source = None
        for index, src in sources.items():
            if bug.bug_id <= int(index):
                source = src['bintest']
                break
        return [source]

    def classpath(self, bug):
        classpath = ""
        workdir = bug.working_directory

        sources = self.project_data[bug.project]["classpath"]
        sources = collections.OrderedDict(
            sorted(sources.items(), key=lambda t: int(t[0])))
        for index, cp in sources.items():
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
        cmd = """export PATH="%s:%s:$PATH";export JAVA_HOME="%s";
        cd %s;
        defects4j export -p cp.test 2> /dev/null;
        """ % (JAVA8_HOME,
               self._get_benchmark_path(),
               os.path.join(JAVA8_HOME, '..'),
               bug.working_directory)
        try:
            lib_output = subprocess.check_output(cmd, shell=True, stderr=FNULL)
            libs_split = str(lib_output, 'utf-8').split(':')
            for lib_str in libs_split:
                lib = os.path.basename(lib_str)
                if lib[-4:] == ".jar":
                    libs.append(lib)
            libs_path = os.path.join(
                self.path, "framework", "projects", bug.project, "lib")
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
        except subprocess.CalledProcessError as e:
            print('----------ERROR defects4j classpath------------')
            print(e.output)
            print('----------cmd--------------')
            print(cmd)
            print('----------end--------------')

    def compliance_level(self, bug):
        return self.project_data[bug.project]["complianceLevel"][str(bug.bug_id)]["source"]


add_benchmark("Defects4J", Defects4J)
