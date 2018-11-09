import os
import json
import time
import random

from config import WORKING_DIRECTORY, REPAIR_ROOT
from config import DATA_PATH
from config import REPAIR_TOOL_FOLDER

LOCK_FILE = "LOCK_BUGS_INIT"


def is_lock():
    return os.path.exists(os.path.join(REPAIR_ROOT, LOCK_FILE))


def wait_lock():
    while is_lock():
        time.sleep(random.randrange(1, 5)/10)


def lock():
    f = open(os.path.join(REPAIR_ROOT, LOCK_FILE), "w+")
    f.close()
    pass


def unclock():
    os.remove(os.path.join(REPAIR_ROOT, LOCK_FILE))


class RepairTool(object):
    def __init__(self, name, config_name):
        self.data = None
        self.main = None
        self.jar = None
        self.name = name
        self.config_name = config_name
        self.parseData()
        pass

    def parseData(self):
        path = os.path.join(DATA_PATH, 'repair_tools', self.config_name + '.json')
        with open(path) as data_file:
            self.data = json.load(data_file)
            self.main = self.data["main"]
            self.jar = os.path.join(REPAIR_TOOL_FOLDER, self.data["jar"])

    def init_bug(self, bug, bug_path):
        wait_lock()
        lock()
        try:
            bug.checkout(bug_path)
            bug.compile()
            # bug.run_test()
        finally:
            unclock()
        pass

    def get_info(self, bug, bug_path):
        pass

    def repair(self, bug):
        bug_path = os.path.join(WORKING_DIRECTORY, "%s_%s" % (bug.project, bug.bug_id))
        self.init_bug(bug, bug_path)

        self.get_info(bug, bug_path)
        pass

    def __str__(self):
        return self.name
