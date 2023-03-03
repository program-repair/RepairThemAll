import json
import os
import shutil
from core.database.schema import Result
from core.tools.java_lang import get_node_by_position, load_ast_nodes, load_origin_code_node
from core.tools.log import printlog
from core.tools.patch import load_patch_file
from core.tools.persist import write_to_file
from core.tools.tokenizer import number_of_tokens

from core.utils import get_benchmark


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


def build_result_template(args, bug_id):
    result_template = Result()
    result_template.model = args.model
    result_template.benchmark = args.benchmark
    result_template.project = args.project
    result_template.bug_id = bug_id
    result_template.request_type = 'SINGLE_FUNCTION'
    result_template.sample_number = 0
    return result_template


def is_compile_success(compile_result):
    return not 'BUILD FAILURE' in compile_result


def is_test_success(test_result):
    if test_result['errors'] > 0 or test_result['failures'] > 0:
        return False
    return True


def handle_buggy_version(working_directory, project, bug_id, benchmark):
    bug = benchmark.get_bug('{}_{}'.format(project, bug_id))

    # Checkout the buggy version
    buggy_bug_path = os.path.join(working_directory,
                                  "%s_%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id, 'buggy'))
    printlog('buggy_bug_path', buggy_bug_path)
    if os.path.exists(buggy_bug_path):
        print('will clean folder', buggy_bug_path)
        shutil.rmtree(buggy_bug_path)
    # True for buggy version, False for fixed version
    bug.checkout(buggy_bug_path, True)
    printlog('--run test on the buggy version--')
    buggy_test_output = bug.run_test()
    printlog('--test result of the buggy version--', buggy_test_output)
    return bug, buggy_test_output


def handle_fixed_version(working_directory, project, bug_id, benchmark):
    bug = benchmark.get_bug('{}_{}'.format(project, bug_id))

    # Checkout the fixed version
    fixed_bug_path = os.path.join(working_directory,
                                  "%s_%s_%s_%s" % (bug.benchmark.name, bug.project, bug.bug_id, 'fixed'))
    printlog('fixed_bug_path', fixed_bug_path)
    if os.path.exists(fixed_bug_path):
        print('will clean folder', fixed_bug_path)
        shutil.rmtree(fixed_bug_path)
    # True for buggy version, False for fixed version
    bug.checkout(fixed_bug_path, False)
    printlog('--run test on the fixed version--')
    fixed_test_output = bug.run_test()
    printlog('--test result of the fixed version--', fixed_test_output)
    return bug, fixed_test_output


def load_code_node(buggy_file_path, fixed_file_path, countable_diffs):
    buggy_node, i = load_origin_code_node(
        buggy_file_path, countable_diffs[0].sorted_changes())
    fixed_nodes = load_ast_nodes(fixed_file_path)
    fixed_node = get_node_by_position(fixed_nodes, buggy_node, i)
    return buggy_node, fixed_node


def ask_codex_for_single_bug(benchmark, args, bug_id, fixa_config):
    try:
        # build a result template that will be used to save the result
        result_template = build_result_template(args, bug_id)
        # run buggy version
        buggy_bug, result_template.buggy_test_output = handle_buggy_version(
            args.working_directory, args.project, bug_id, benchmark)
        # run fixed version
        fixed_bug, result_template.fixed_test_output = handle_fixed_version(
            args.working_directory, args.project, bug_id, benchmark)

        bug_dir = os.path.join(args.working_directory, "%s_%s_%s" %
                               (benchmark, args.project, bug_id))
        patch_file_path = os.path.join(
            bug_dir + '_buggy/', '.bugs-dot-jar/developer-patch.diff')
        countable_diffs, _ = load_patch_file(None, patch_file_path)

        fixed_bug_path = bug_dir + "_fixed/" + countable_diffs[0].file_path
        buggy_bug_path = bug_dir + "_buggy/" + countable_diffs[0].file_path

        # have to reverse the order of the two files in Bugs.jar
        buggy_node, fixed_node = load_code_node(
            buggy_bug_path, fixed_bug_path, countable_diffs)

        result_template.bug_start_pos = buggy_node.start_pos
        result_template.bug_end_pos = buggy_node.end_pos

        result_template.buggy_code_chunk = buggy_node.code_lines_str()
        result_template.buggy_code_token = number_of_tokens(
            result_template.buggy_code_chunk)
        result_template.fixed_code_chunk = fixed_node.code_lines_str()
        result_template.fixed_code_token = number_of_tokens(
            result_template.fixed_code_chunk)

        output = []
        output.append('project: ' + args.project)
        output.append('bug_id: ' + str(bug_id))
        output.append('buggy_file_path: ' + buggy_bug_path)
        output.append('buggy_code_chunk: ' + result_template.buggy_code_chunk)
        output.append('buggy_code_token: ' +
                      str(result_template.buggy_code_token))
        output.append('fixed_code_chunk: ' + result_template.fixed_code_chunk)
        output.append('fixed_code_token: ' +
                      str(result_template.fixed_code_token))
        output.append('bug_start_pos: ' + str(result_template.bug_start_pos))
        output.append('bug_end_pos: ' + str(result_template.bug_end_pos))
        output.append('buggy_test_output: ' +
                      str(result_template.buggy_test_output))
        output.append('fixed_test_output: ' +
                      str(result_template.fixed_test_output))

        output_dir = os.path.join(args.working_directory, 'bugs-dot-jar-data')
        write_to_file(output_dir + '/{}-{}.txt'.format(args.project, bug_id),
                      '\n'.join(output))

        # TODO: pause to build prompt with smallest example
        # result_template = build_prompt(result_template, fixed_bug, buggy_node, fixa_config, bug_dir)

        # TODO: calculate number of requests
        # result_template, request_counter = build_request_params(result_template, fixa_config)
        # TODO: send prompt to codex
    except Exception as e:
        print('error', e)
        return None
