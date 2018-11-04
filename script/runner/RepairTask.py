class RepairTask(object):

    def __init__(self, tool, benchmark, bug):
        self.tool = tool
        self.benchmark = benchmark
        self.bug = bug
        self.status = None
        self.id = None
        self.results = None

    def run(self):
        return self.tool.repair(self)