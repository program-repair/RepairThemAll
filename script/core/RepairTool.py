import os
import json

from config import WORKING_DIRECTORY
from config import DATA_PATH
from config import REPAIR_TOOL_FOLDER


class RepairTool(object):
    def __init__(self, name, config_name):
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
        bug.checkout(bug_path)
        bug.compile()
        # bug.run_test()
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
