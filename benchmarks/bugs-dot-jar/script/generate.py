import os
import json

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")

patches = json.load(open(os.path.join(DATA_PATH, "patches.json")))

for project_name in patches:
    for (commit_id) in patches[project_name].keys():
        patches[project_name][commit_id[0:8]
                              ] = patches[project_name][commit_id]
bugs = []
for project_name in os.listdir(DATA_PATH):
    project_path = os.path.join(DATA_PATH, project_name)
    if not os.path.isdir(project_path):
        continue
    for bug_id in os.listdir(project_path):
        with open(os.path.join(project_path, bug_id)) as fd:
            bug = json.load(fd)
            bug['project'] = project_name
            bug['files'] = bug['patch'].count("+++ b/")
            bug['linesAdd'] = 0
            bug['linesRem'] = 0
            for line in bug['patch'].split("\n"):
                if len(line) == 0:
                    continue
                lineType = line[0]
                line = line[1::].strip()
                if len(line) > 0 and (line[0:3] == '++ ' or line[0:3] == '-- ' or line[0] == '*' or line[0:2] == '/*' or line[0:2] == '*/' or line[0:2] == '//'):
                    continue
                if lineType == '+':
                    bug['linesAdd'] += 1
                if lineType == '-':
                    bug['linesRem'] += 1

            #bug['linesRem'] = bug['patch'].count("\n-") - bug['files']
            bug['singleLine'] = (bug['linesAdd'] == 1 and bug['linesRem'] == 0) or (
                bug['linesAdd'] == 0 and bug['linesRem'] == 1)
            if project_name in patches and bug["commit"] in patches[project_name]:
                for repair_tool in patches[project_name][bug["commit"]]:
                    bug['rt' + repair_tool] = True
            bugs += [bug]

print "Processed %d bugs" % len(bugs)
with open(os.path.join(DATA_PATH, "..", "docs", "data", "bugs.json"), "w") as fd:
    json.dump(bugs, fd)
