import time
import os

from core.RepairTool import RepairTool
from core.Benchmark import Benchmark
from core.Bug import Bug

from config import OUTPUT_PATH


class RepairTask(object):

    def __init__(self, tool, benchmark, bug):
        """"
        :type tool: RepairTool
        :type benchmark: Benchmark
        :type bug: Bug
        """
        self.tool = tool
        self.benchmark = benchmark
        self.bug = bug
        self.status = None
        self.id = None
        self.results = None
        self.starting_date = None
        self.end_date = None

    def run(self):
        self.starting_date = time.time()
        return self.tool.repair(self)

    def log_dir(self):
        return os.path.join(OUTPUT_PATH, self.bug.benchmark.name, self.bug.project, str(self.bug.bug_id), self.tool.name, str(self.tool.seed))
