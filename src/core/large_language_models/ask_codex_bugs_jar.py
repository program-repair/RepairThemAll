import json


def get_bugs_config(project, bug_id):
    bug_config_file_path = 'benchmarks/bugs-dot-jar/data/{}/{}.json'.format(
        project, bug_id)
    f = open(bug_config_file_path)
    bug_data = json.load(f)
    f.close()
    return bug_data


def save_bug_config(project, id, bug_data):
    bug_config_file_path = 'benchmarks/bugs-dot-jar/data/{}/{}.json'.format(
        project, id)
    f = open(bug_config_file_path, 'w')
    json.dump(bug_data, f, indent=4)
    f.close()


def count_eligible_bugs(projects, total_bugs):
    total_eligible_bugs = 0
    for project in projects:
        project_eligible_bugs = 0
        for i in range(total_bugs[project]):
            bug_commit_file_path = 'benchmarks/bugs-dot-jar/data/{}/{}.json'.format(
                project, i + 1)
            f = open(bug_commit_file_path)
            bug_data = json.load(f)
            if bug_data['files'] == 1:
                project_eligible_bugs += 1
                total_eligible_bugs += 1
            f.close()
        print('project:', project)
        print('project total bugs:', total_bugs[project])
        print('project eligible bugs:', project_eligible_bugs)

    print('-' * 80)
    print('total eligible bugs:', total_eligible_bugs)


def try_to_compile(project, bug_id):
    # checkout the bug first
    pass
