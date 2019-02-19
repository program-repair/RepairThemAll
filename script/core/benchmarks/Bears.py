import json
import os
import subprocess

from config import REPAIR_ROOT, DATA_PATH
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

class Bears(Benchmark):
    """Bears Benchmark"""

    def __init__(self):
        super(Bears, self).__init__("Bears")
        self.path = os.path.join(REPAIR_ROOT, "benchmarks", "bears")
        self.project_data = {}
        self.bugs = None
        self.get_bugs()

    def get_bug(self, bug_id):
        bug_id = bug_id.replace("_", "-")
        separator = "-"
        splitted = bug_id.split(separator)

        project = splitted[0]
        if len(splitted) < 3:
            project = "-".join(splitted[:-1])
        else:
            patched = splitted[-1]
            buggy = splitted[-2]
            project = "-".join(splitted[:-2])

        for bug in self.get_bugs():
            if bug.project.lower() == project.lower():
                if len(splitted) < 3 or bug.bug_id.lower() == ("%s-%s" % (buggy, patched)):
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

    def _get_project_info(self, bug):
        try:
            return bug.maven_info
        except AttributeError:
            pass
        local_working_directory = bug.working_directory
        pom_path = bug.info['reproductionBuggyBuild']['projectRootPomPath']
        buggy_build_id = bug.info['builds']['buggyBuild']['id']
        pom_path = pom_path.partition(str(buggy_build_id))[2]
        pom_path = pom_path.replace("/pom.xml", "")
        pom_path = pom_path.replace("/", "", 1)
        if pom_path:
        	local_working_directory = os.path.join(local_working_directory, pom_path)        
        cmd = """cd %s;
mvn com.github.tdurieux:project-config-maven-plugin:1.0-SNAPSHOT:info -q;
""" % (local_working_directory)
        info = json.loads(subprocess.check_output(cmd, shell=True))
        bug.maven_info = info
        return info

    def checkout(self, bug, working_directory):
        branch_id = "%s-%s" % (bug.project, bug.bug_id)

        cmd = "cd " + self.path + "; git reset .; git checkout -- .; git clean -x -d --force; git checkout -f master; git checkout -f " + branch_id
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

        bears_info_path = os.path.join(self.path, "bears.json")
        with open(bears_info_path) as fd:
            bug.info = json.load(fd)

        cmd = "cd " + self.path + "; git log --format=format:%H --grep='Changes in the tests'"
        bug_commit = subprocess.check_output(cmd, shell=True)
        if len(bug_commit) == 0:
            cmd = "cd " + self.path + "; git log --format=format:%H --grep='Bug commit'"
            bug_commit = subprocess.check_output(cmd, shell=True)

        cmd = """cd %s;
git checkout -f %s;
cp -r . %s""" % (
            self.path,
            bug_commit,
            working_directory,
        )
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def compile(self, bug, working_directory):
        local_working_directory = working_directory
        pom_path = bug.info['reproductionBuggyBuild']['projectRootPomPath']
        buggy_build_id = bug.info['builds']['buggyBuild']['id']
        pom_path = pom_path.partition(str(buggy_build_id))[2]
        pom_path = pom_path.replace("/pom.xml", "")
        pom_path = pom_path.replace("/", "", 1)
        if pom_path:
        	local_working_directory = os.path.join(local_working_directory, pom_path)        
        cmd = """cd %s;
export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true;
mvn install -V -B -DskipTests -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true; 
mvn test -DskipTests -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true -Denforcer.skip=true;
mvn dependency:build-classpath -Dmdep.outputFile="classpath.info";
""" % (local_working_directory)
        subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        pass

    def run_test(self, bug, working_directory):
        local_working_directory = working_directory
        pom_path = bug.info['reproductionBuggyBuild']['projectRootPomPath']
        buggy_build_id = bug.info['builds']['buggyBuild']['id']
        pom_path = pom_path.partition(str(buggy_build_id))[2]
        pom_path = pom_path.replace("/pom.xml", "")
        pom_path = pom_path.replace("/", "", 1)
        if pom_path:
        	local_working_directory = os.path.join(local_working_directory, pom_path)
        cmd = """cd %s;
export _JAVA_OPTIONS=-Djdk.net.URLClassPath.disableClassPathURLCheck=true;  
rm -rf .git; git init; git commit -m 'init' --allow-empty;
mvn test -V -B -Denforcer.skip=true -Dcheckstyle.skip=true -Dcobertura.skip=true -DskipITs=true -Drat.skip=true -Dlicense.skip=true -Dfindbugs.skip=true -Dgpg.skip=true -Dskip.npm=true -Dskip.gulp=true -Dskip.bower=true -Djacoco.skip=true -Denforcer.skip=true
""" % (local_working_directory)
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

    def failing_module(self, bug):
        failing_module = bug.info['tests']['failingModule']
        buggy_build_id = str(bug.info['builds']['buggyBuild']['id'])
        try:
            index_build = failing_module.index(buggy_build_id + "/")
            return failing_module[index_build + len(buggy_build_id) + 1:]
        except ValueError:
            return "root"

    def source_folders(self, bug):
        folders = []

        info = self._get_project_info(bug)
        failing_module = self.failing_module(bug)

        for module in info['modules']:
            module_name = module['baseDir'].replace(bug.working_directory + '/', '')
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
        info = self._get_project_info(bug)
        return info['complianceLevel']

add_benchmark("Bears", Bears)