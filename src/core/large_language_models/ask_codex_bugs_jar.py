import json
import os


def get_bugs_config(project):
    bug_commit_entries = os.listdir(
        'benchmarks/bugs-dot-jar/data/{}/'.format(project))
    # for i in range(len(bug_commit_entries)):
    #     print('bug number:', i)
    #     print(bug_commit_entries[i][:-5])
    #     bug_commit_file_path = 'benchmarks/bugs-dot-jar/data/{}/{}'.format(
    #         project, bug_commit_entries[i])
    #     f = open(bug_commit_file_path)
    #     bug_data = json.load(f)
    #     bug_data['bug_id'] = i + 1
    #     for key in bug_data.keys():
    #         print(key, bug_data[key])
    #     f.close()
    #     new_json_file_path = 'benchmarks/bugs-dot-jar/data/{}/{}.json'.format(
    #         project, i + 1)
    #     with open(new_json_file_path, "w") as outfile:
    #         json.dump(bug_data, outfile, sort_keys=True, indent=4)
