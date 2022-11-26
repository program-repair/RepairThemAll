import json
import subprocess
import os
import xml.etree.ElementTree as ET

from config import JAVA8_HOME, MAVEN_BIN


class Benchmark(object):
    """Benchmark"""

    def __init__(self, name):
        self.name = name
        pass

    def _get_project_info(self, bug):
        try:
            return bug.maven_info
        except AttributeError:
            pass
        cmd = """cd %s;
export PATH="%s:$PATH";
export JAVA_HOME="%s";
mvn com.github.tdurieux:project-config-maven-plugin:1.0-SNAPSHOT:info -q;
""" % (bug.working_directory, MAVEN_BIN, os.path.join(JAVA8_HOME, '..'))
        info = json.loads(subprocess.check_output(cmd, shell=True))
        bug.maven_info = info
        return info

    def checkout(self, bug, working_directory, buggy_version=True):
        pass

    def compile(self, bug, working_directory):
        pass

    def run_test(self, bug, working_directory, test=None):
        pass

    def get_maven_test_results(self, bug, working_directory):
        errors = 0
        failures = 0
        tests = 0
        skips = 0
        for rootPath, dirs, files in os.walk(working_directory, topdown=False):
            if "surefire-reports" not in rootPath:
                continue
            for name in files:
                if ".xml" not in name:
                    continue
                try:
                    tree = ET.parse(os.path.join(
                        working_directory, rootPath, name))
                    root = tree.getroot()
                    if 'errors' in root.attrib:
                        errors += int(root.attrib['errors'])
                    if 'failures' in root.attrib:
                        failures += int(root.attrib['failures'])
                    if 'failed' in root.attrib:
                        failures += int(root.attrib['failed'])
                    if 'tests' in root.attrib:
                        tests += int(root.attrib['tests'])
                    if 'skipped' in root.attrib:
                        skips += int(root.attrib['skipped'])
                except:
                    continue
        return {'tests': tests, 'failures': failures, 'errors': errors, 'skips': skips}

    def classpath(self, bug):
        pass

    def compliance_level(self, bug):
        pass

    def source_folders(self, bug):
        pass

    def test_folders(self, bug):
        pass

    def parse_bug_snippet(self, bug):
        # read line number from a java patch file
        pass

    def __str__(self):
        return self.name
