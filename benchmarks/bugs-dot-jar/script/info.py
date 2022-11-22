import os
import json

from config import DATA_PATH


def info(project, commit_id):
    path_bug = os.path.join(DATA_PATH, project, commit_id + ".json")
    if os.path.exists(path_bug):
        with open(path_bug) as fd:
            return json.load(fd)
    return None


def print_info(data):
    print("""
Project: %s
Jira ID: %s
Commit ID: %s

# Test: %d
# Failure: %d
# Error: %d
    """) % (
        data["project"],
        data["jira_id"],
        data["commit"],
        data["nb_test"],
        data["nb_failure"],
        data["nb_error"],
    )
    pass


def info_args(args):
    data = info(args.project, args.id)
    if data is None:
        print("[Error] info of %s %s is not found" % (args.project, args.id))
        return None
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print_info(data)
