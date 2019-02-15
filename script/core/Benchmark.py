import json
import subprocess

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
mvn com.github.tdurieux:project-config-maven-plugin:1.0-SNAPSHOT:info -q;
""" % (bug.working_directory)
        info = json.loads(subprocess.check_output(cmd, shell=True))
        bug.maven_info = info
        return info

    def checkout(self, bug, working_directory):
        pass

    def compile(self, bug, working_directory):
        pass

    def run_test(self, bug, working_directory):
        pass

    def classpath(self, bug):
        pass

    def compliance_level(self, bug):
        pass

    def source_folders(self, bug):
        pass

    def test_folders(self, bug):
        pass

    def __str__(self):
        return self.name
