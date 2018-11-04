from runner.RepairTask import RepairTask


class LocalRunner(object):

    def __init__(self, tasks):
        """
        :type tasks: list of RepairTask
        """
        self.tasks = tasks
        self.finished = []
        self.running = []
        self.waiting = []

    def execute(self):
        for task in self.tasks:
            task.run()
