class LocalRunner(object):

    def __init__(self, tasks):
        self.tasks = tasks
        self.finished = []
        self.running = []
        self.waiting = []

    def execute(self):
        for task in self.tasks:
            task.run()
