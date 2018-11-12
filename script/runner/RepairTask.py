import time

from core.RepairTool import RepairTool
from core.Benchmark import Benchmark
from core.Bug import Bug


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
