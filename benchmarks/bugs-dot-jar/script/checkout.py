import os
import subprocess
import shutil

from config import REPOSITORIES_PATH
from config import BUGS_PATH

from info import info


def create_bug(project_path, branch_name, destination):
    FNULL = open(os.devnull, 'w')

    cmd = "cd %s; git checkout checkout -- .; git checkout %s;" % (
        project_path, branch_name)
    subprocess.call(cmd, shell=True, stdout=FNULL, stderr=FNULL)
    shutil.copytree(project_path, destination)
    # generate a simplified patch
    cmd = "cd %s;  git apply .bugs-dot-jar/developer-patch.diff; git diff --ignore-all-space --minimal --ignore-blank-lines;" % destination
    human_patch = subprocess.check_output(cmd, shell=True)
    cmd = "cd %s;  git checkout -- .;" % destination
    subprocess.call(cmd, shell=True, stdout=FNULL, stderr=FNULL)
    with open(os.path.join(destination, ".bugs-dot-jar", "developer-patch.diff"), 'w') as fd:
        fd.write(human_patch)
    if os.path.exists(os.path.join(destination, ".git")):
        shutil.rmtree(os.path.join(destination, ".git"))


def checkout(bug, destination):
    if bug is None:
        print("[Error] The bug is not found.")
        return
    if destination is None:
        destination = os.path.join(BUGS_PATH, bug["project"], bug["commit"])
    create_bug(os.path.join(REPOSITORIES_PATH, bug["project"]), "remotes/origin/bugs-dot-jar_%s-%s_%s" % (
        bug["project"].upper(), bug["jira_id"], bug["commit"]), destination)
    pass


def checkout_args(args):
    checkout(info(args.project, args.id), args.destination)
    pass


def checkout_all_args(args):
    pass
