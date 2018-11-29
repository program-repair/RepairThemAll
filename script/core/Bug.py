import json
import os

from core.Benchmark import Benchmark


class Bug(object):
    """A bug"""

    def __init__(self, benchmark, project, bug_id):
        """
        :param benchmark:
        :type benchmark: Benchmark
        :param project:
        :param bug_id:
        """
        self.project = project
        self.bug_id = bug_id
        self.benchmark = benchmark
        self.working_directory = None

    def _get_project_data(self):
        if self.project_data is not None:
            return self.project_data

        project_data_path = os.path.join(self.benchmark.get_data_path(), "%s.json" % self.project.lower())
        with open(project_data_path) as fd:
            self.project_data = json.load(fd)
            return self.project_data

    def checkout(self, working_directory):
        self.working_directory = working_directory

        self.benchmark.checkout(self, working_directory)
        pass

    def compile(self):
        return self.benchmark.compile(self, self.working_directory)

    def run_test(self):
        return self.benchmark.run_test(self, self.working_directory)

    def failing_tests(self):
        return self.benchmark.failing_tests(self)

    def source_folders(self):
        return self.benchmark.source_folders(self)

    def test_folders(self):
        return self.benchmark.test_folders(self)

    def bin_folders(self):
        return self.benchmark.bin_folders(self)

    def test_bin_folders(self):
        return self.benchmark.test_bin_folders(self)

    def classpath(self, repair_task):
        return self.benchmark.classpath(repair_task)

    def compliance_level(self):
        return self.benchmark.compliance_level(self)

    def __str__(self):
        return "%s_%s_%s" % (self.benchmark, self.project, self.bug_id)
