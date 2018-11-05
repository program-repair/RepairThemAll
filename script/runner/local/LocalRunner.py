from Queue import Queue
from threading import Thread
import time

from runner.RepairTask import RepairTask
from runner.Runner import Runner
from runner.renderer.BashRenderer import BashRenderer
from config import LOCAL_THREAD


class RunnerWorker(Thread):
    def __init__(self, local_runner, callback):
        Thread.__init__(self)
        self.local_runner = local_runner
        self.callback = callback
        self.daemon = True

    def run(self):
        pool = RepairThreadPool(LOCAL_THREAD)

        for task in self.local_runner.tasks:
            self.local_runner.running += [task]
            task.status = "WAITING"
            pool.add_repair(task, self.callback)

        pool.wait_completion()


class RepairWorker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            (task, callback) = self.tasks.get()
            task.status = "STARTED"
            try:
                task.run()
            except Exception, e:
                task.status = "ERROR"
                print e
            finally:
                if callback is not None:
                    callback(task)
                self.tasks.task_done()


class RepairThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            RepairWorker(self.tasks)

    def add_repair(self, task, callback):
        """Add a task to the queue"""
        self.tasks.put((task, callback))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


class LocalRunner(Runner):

    def __init__(self, tasks):
        """
        :type tasks: list of RepairTask
        """
        super(LocalRunner, self).__init__(tasks)
        self.tasks = tasks
        self.finished = []
        self.running = []
        self.waiting = []

    def repair_done(self, task):
        if task.status is "STARTED":
            task.status = "DONE"
        task.end_date = time.time()
        self.finished += [task]
        self.running.remove(task)
        pass

    def execute(self):
        worker = RunnerWorker(self, self.repair_done)
        renderer = BashRenderer(self)
        worker.start()

        while worker.is_alive():
            renderer.render()
            time.sleep(1)

        renderer.render_final_result()
