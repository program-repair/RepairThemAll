import os
import shutil
import subprocess
import json

REPOSITORIES_PATH = "/mnt/secondary/"
DESTINATION = "/mnt/secondary/defects4j4repair"
BUGS_PATH = os.path.join(REPOSITORIES_PATH, "projects_fix")

def create_branch(bug_id, bug_path):
    branch_name = "%s_patched" % bug_id
    cmd = "cd %s; git checkout %s; git checkout -b %s; cp -r %s/* .; cp %s/.defects4j.config .; git add -f .; git commit -m 'patch %s'; git checkout master;" % (
        DESTINATION,
        "%s_buggy_minimized" % bug_id,
        branch_name,
        bug_path,
        bug_path,
        bug_id
    )
    subprocess.check_output(cmd, shell=True)
    pass

for project_name in sorted(os.listdir(BUGS_PATH)):
    project_path = os.path.join(BUGS_PATH, project_name)
    if not os.path.exists(project_path):
        continue
    if not os.path.isdir(project_path):
        continue
    for bug_id in sorted(os.listdir(project_path)):
        bug_path = os.path.join(project_path, bug_id)
        if not os.path.exists(bug_path):
            continue
        if not os.path.isdir(bug_path):
            continue
        create_branch(bug_id, bug_path)

    