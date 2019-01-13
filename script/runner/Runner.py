import datetime


class Runner(object):

    def __init__(self, tasks, args):
        """
        :type tasks: list of RepairTask
        """
        self.tasks = tasks
        self.finished = []
        self.running = []
        self.waiting = []
        self.args = args
        self.end_time = None
        if args.end_time is not None:
            hours, minutes = args.end_time.split(':')
            now = datetime.datetime.now()
            self.end_time = now.replace(hour=int(hours), minute=int(minutes), second=0)
            if self.end_time < now:
                # set the end date to tomorrow
                self.end_time += datetime.timedelta(days=1)

    def is_end_time(self):
        if self.end_time is None:
            return False
        return self.end_time > datetime.datetime.now()

