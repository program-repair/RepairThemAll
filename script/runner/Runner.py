class Runner(object):

    def __init__(self, tasks):
        """
        :type tasks: list of RepairTask
        """
        self.tasks = tasks
        self.finished = []
        self.running = []
        self.waiting = []
