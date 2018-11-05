import time
import subprocess
import json
import os
import re

from runner.RepairTask import RepairTask
from runner.Runner import Runner
from runner.renderer.BashRenderer import BashRenderer
from config import REPAIR_ROOT, OUTPUT_PATH, GRID5K_MAX_NODE


class Grid5kRunner(Runner):

    def __init__(self, tasks):
        """
        :type tasks: list of RepairTask
        """
        super(Grid5kRunner, self).__init__(tasks)

    def repair_done(self, task):
        if task.status is "STARTED":
            task.status = "DONE"
        task.end_date = time.time()
        self.finished += [task]
        self.running.remove(task)
        pass

    def get_running(self):
        cmd = 'oarstat --json -u `whoami`'

        devnull = open('/dev/null', 'w')
        try:
            cmd_output = subprocess.check_output(cmd, shell=True, stdin=None, stderr=devnull)
            jobs = json.loads(cmd_output)
            running_ids = []
            waiting_ids = []
            for job_id in jobs:
                if jobs[job_id]['state'] == "Running":
                    running_ids.append(job_id)
                else:
                    waiting_ids.append(job_id)

            for task in self.running:
                if task.id not in running_ids:
                    self.finished.append(task)
                    task.end_date = time.time()
                    task.status = "Done"
                    self.running.remove(task)

            for task in self.waiting:
                if task.id not in waiting_ids:
                    self.waiting.remove(task)
                if task.id in running_ids:
                    task.status = "STARTED"
                    task.starting_date = time.time()
                    self.running.append(task)

        except subprocess.CalledProcessError:
            pass
        finally:
            return self.running

    def start_task(self, task):
        """
        :param task:
        :type task: RepairTask
        :return:
        """

        log_root_path = os.path.join(OUTPUT_PATH, task.benchmark.name, task.bug.project, str(task.bug.bug_id),
                                     task.tool.name,
                                     str(task.tool.seed))

        stdout_log = os.path.join(log_root_path, 'grid5k.stdout.log')
        stderr_log = os.path.join(log_root_path, 'grid5k.stderr.log')

        if not os.path.exists(log_root_path):
            os.makedirs(log_root_path)

        node_cmd_args = "%s %s --benchmark %s --id %s" % (
            os.path.join(REPAIR_ROOT, 'script', 'repair.py'),
            task.tool.name,
            task.benchmark.name,
            "%s-%s" % (task.bug.project, task.bug.bug_id)
        )
        node_cmd = "sudo-g5k apt-get install -y maven; python %s" % node_cmd_args

        cmd = "oarsub -l nodes=1,walltime=%s -O %s -E %s \"%s\"" % (
            "2:00",
            stdout_log,
            stderr_log,
            node_cmd)
        devnull = open('/dev/null', 'w')

        cmd_output = subprocess.check_output(cmd, shell=True, stdin=None, stderr=devnull)
        m = re.search('OAR_JOB_ID=([0-9]+)', cmd_output)
        if m:
            task.id = m.group(1)
            task.status = "WAITING"
            self.waiting.append(task)

    def execute(self):
        renderer = BashRenderer(self)
        to_run = self.tasks[:]
        while len(to_run) > 0 or len(self.running) > 0 or len(self.waiting) > 0:
            if len(to_run) > 0 and len(self.running) + len(self.waiting) < GRID5K_MAX_NODE:
                self.start_task(to_run.pop())
            time.sleep(1)
            renderer.render()
            self.get_running()

        renderer.render_final_result()
