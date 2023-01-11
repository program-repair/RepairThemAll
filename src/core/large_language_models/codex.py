import copy
import os
import time
from dotenv import dotenv_values
import openai
from core.database.engine import save
from core.database.schema import Result
from core.tools.java_lang import get_node_by_position, load_ast_nodes, load_fixed_code_node
from core.tools.patch import load_patch_file, read_patch_file
from core.tools.persist import write_to_file
from core.tools.prompt import generate_prompt
from core.tools.tokenizer import calculate_request_counter, number_of_tokens
from core.utils import get_benchmark


config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"
EXAMPLE_BUGGY_FILEPATH = 'data/example/codex_prompt_example_buggy.source'
EXAMPLE_FIXED_FILEPATH = 'data/example/codex_prompt_example_fixed.source'
PROJECT_EXAMPLE_BUGGY_PATH_FORMAT = 'data/example/codex_project_example_{}_buggy.source'
PROJECT_EXAMPLE_FIXED_PATH_FORMAT = 'data/example/codex_project_example_{}_fixed.source'

STOP_SIGN = "###"


def load_code_node(fixed_file_path, buggy_file_path, countable_diffs):
    fixed_node, i = load_fixed_code_node(
        fixed_file_path, countable_diffs[0].sorted_changes())
    buggy_nodes = load_ast_nodes(buggy_file_path)
    buggy_node = get_node_by_position(buggy_nodes, fixed_node, i)
    return fixed_node, buggy_node


def request_codex_code_complition(prompt, request_params):
    # https://beta.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        prompt=prompt,
        model=request_params['model'],
        temperature=request_params['temperature'],
        max_tokens=request_params['max_tokens'],
        top_p=request_params['top_p'],
        frequency_penalty=request_params['frequency_penalty'],
        presence_penalty=request_params['presence_penalty'],
        stop=request_params['stop'],
        n=request_params['n'],
    )
    print('--->', response)
    return response


def apply_text_to_fixed_version(fixed_bug_path, response_text, fixed_node):
    print('fixed_bug_path: ', fixed_bug_path)
    print('fixed_node: ', fixed_node)
    print('response_text: ', response_text)
    original_fixed_bug_lines = []
    try:
        response_text_lines = response_text.split("\n")
        with open(fixed_bug_path, 'r') as file:
            fixed_bug_lines = file.readlines()
        original_fixed_bug_lines = copy.deepcopy(fixed_bug_lines)
        new_fixed_bug_file = "".join(fixed_bug_lines[0:fixed_node.start_pos - 1]) + \
            "\n".join(response_text_lines) + \
            "".join(fixed_bug_lines[fixed_node.end_pos:])
        write_to_file(fixed_bug_path, new_fixed_bug_file)
        return True, None, original_fixed_bug_lines
    except Exception as e:
        print('Error: ', e)
        print('fixed_bug_path: ', fixed_bug_path)
        return False, e, original_fixed_bug_lines


def get_fixed_bug_path(bug_dir, patch_file_path):
    countable_diffs, _ = load_patch_file(None, patch_file_path)
    return bug_dir + "_fixed/" + countable_diffs[0].file_path


# revert fixed bug file after testing codex response
def revert_response_to_fixed_version(original_buy_lines, working_directory, bug, patch_file_path):
    print('revert fixed bug file after testing codex response')
    bug_dir = os.path.join(working_directory, "%s_%s_%s" %
                           (bug.benchmark, bug.project, bug.bug_id))
    fixed_bug_path = get_fixed_bug_path(bug_dir, patch_file_path)
    write_to_file(fixed_bug_path, ''.join(original_buy_lines))


def checkout_bug(benchmark, working_directory, project, bug_id, version):
    bug_identifier = project + '_' + bug_id

    bug_path = os.path.join(working_directory,
                            "%s_%s_%s_%s" % (benchmark.name, project, bug_id, version))

    print('bug_identifier: ', bug_identifier)
    bug = benchmark.get_bug(bug_identifier)
    print('bug: ', bug)
    is_buggy_version = version == 'buggy'
    bug.checkout(bug_path, is_buggy_version)

    return bug


def fix_single_bug(args, bug_id, fixa_config):
    # Only support Codex with Defects4J for now
    if args.model != 'Codex' or args.benchmark != 'Defects4J':
        print('Only support Codex with Defects4J for now')
        exit(1)

    benchmark = get_benchmark(args.benchmark)

    # checkout fixed bug
    try:
        fixed_bug = checkout_bug(
            benchmark, args.working_directory, args.project, bug_id, 'fixed')
        if fixa_config['compile']:
            fixed_bug.compile()
        if fixa_config['test']:
            fixed_bug.run_test()
    except Exception as e:
        print('-------bug {} {} does not exist or deprecated-------\n'.format(args.project, bug_id), e)
        return

    # checkout buggy bug
    buggy_bug = checkout_bug(
        benchmark, args.working_directory, args.project, bug_id, 'buggy')
    if fixa_config['compile']:
        buggy_bug.compile()
    if fixa_config['test']:
        buggy_bug.run_test()

    # save 'result' to database
    result_template = Result()
    result_template.model = args.model
    result_template.benchmark = args.benchmark
    result_template.project = args.project
    result_template.bug_id = bug_id
    result_template.request_type = 'SINGLE_FUNCTION'
    result_template.sample_number = 0

    # read patch file
    patch_file_path = 'benchmarks/defects4j/framework/projects/{}/patches/{}.src.patch'.format(
        args.project, bug_id)
    countable_diffs, patch_text = read_patch_file(patch_file_path)
    result_template.patch = patch_text
    if len(countable_diffs) > 1:
        result_template.result_type = 'ERROR'
        result_template.error_message = str("Skip, more than one file changed")
        save(result_template)
        return

    # prepare fixed and buggy code ast node
    bug_dir = os.path.join(args.working_directory, "%s_%s_%s" %
                           (fixed_bug.benchmark, fixed_bug.project, bug_id))
    fixed_bug_path = bug_dir + "_fixed/" + countable_diffs[0].file_path
    buggy_bug_path = bug_dir + "_buggy/" + countable_diffs[0].file_path
    fixed_node, buggy_node = load_code_node(
        fixed_bug_path, buggy_bug_path, countable_diffs)

    result_template.buggy_code_chunk = buggy_node.code_lines_str()
    result_template.buggy_code_token = number_of_tokens(
        result_template.buggy_code_chunk)
    result_template.fixed_code_chunk = fixed_node.code_lines_str()
    result_template.fixed_code_token = number_of_tokens(
        result_template.fixed_code_chunk)

    # run original fixed version unit tests
    template_fixed_complied_output = fixed_bug.compile()
    if template_fixed_complied_output.count('OK') == 2:
        _, fixed_test_output = fixed_bug.run_test()
        result_template.fixed_test_output = fixed_test_output
    else:
        result_template.fixed_test_output = 'Compile error'

    # run buggy code against fixed unit tests, then revert the source to the fixed code
    applied, error, original_func_lines = apply_text_to_fixed_version(
        fixed_bug_path, buggy_node.code_lines_str(), fixed_node)
    if applied:
        template_buggy_complied_output = fixed_bug.compile()
        if template_buggy_complied_output.count('OK') == 2:
            _, buggy_test_output = fixed_bug.run_test()
            result_template.buggy_test_output = buggy_test_output
        else:
            result_template.buggy_test_output = 'Compile error'
        revert_response_to_fixed_version(
            original_func_lines, args.working_directory, fixed_bug, patch_file_path)

    # build prompt
    project_buggy_path = PROJECT_EXAMPLE_BUGGY_PATH_FORMAT.format(
        fixed_bug.project)
    project_fixed_path = PROJECT_EXAMPLE_FIXED_PATH_FORMAT.format(
        fixed_bug.project)
    smallest_bug_example_id = int(fixed_bug._get_project_data()['smallestBug'])
    include_project_specific_example = smallest_bug_example_id != 0 and smallest_bug_example_id != int(
        fixed_bug.bug_id)
    output_file_path = 'output/{}'.format(bug_dir.split('/')[-1])
    prompt, prompt_size, bug_size = generate_prompt(STOP_SIGN, EXAMPLE_BUGGY_FILEPATH, EXAMPLE_FIXED_FILEPATH,
                                                    project_buggy_path, project_fixed_path, buggy_node, fixa_config['include_document'], fixa_config['include_comments'], include_project_specific_example)
    write_to_file(output_file_path + '.codex_prompt', prompt)
    result_template.prompt_text = prompt
    result_template.prompt_size = prompt_size

    # calculate number of requests
    request_counter, n_value, max_completion_size = calculate_request_counter(
        fixa_config['sample'], fixa_config['completion_ratio'], prompt_size, bug_size)
    print('request_counter: ', request_counter)
    print('n_value: ', n_value)
    print('max_completion_size: ', max_completion_size)
    request_params = {
        'model': CODEX_MODEL,
        'temperature': 0.8,
        'max_tokens': max_completion_size,
        'top_p': 0.95,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
        'stop': [STOP_SIGN],
        'n': n_value,
    }
    result_template.request_params = request_params
    result_template.prompt_params = fixa_config

    # send requests to Codex
    sample_number = 0
    for i in range(request_counter):
        response = request_codex_code_complition(prompt, request_params)
        for choice in response.choices:  # type: ignore
            sample_result = copy.deepcopy(result_template)
            sample_number += 1
            sample_result.sample_number = sample_number
            print('choice: ', choice.text)
            if choice.finish_reason == 'length':
                sample_result.result_type = 'LENGTH'
                save(sample_result)
            elif choice.finish_reason == 'stop':
                sample_result.result_type = 'STOP'
                sample_result.respond_code_chunk = choice.text
                sample_result.respond_code_token = number_of_tokens(
                    choice.text)
                # apply the choice to the code
                applied, error, original_func_lines = apply_text_to_fixed_version(
                    fixed_bug_path, choice.text, fixed_node)
                if applied:
                    sample_result.result_type = 'APPLIED'
                    compiled_output = fixed_bug.compile()
                    sample_result.respond_compiled_output = compiled_output
                    if compiled_output.count('OK') == 2:
                        sample_result.result_type = 'COMPILED_SUCCESS'
                    success, test_output = fixed_bug.run_test()
                    sample_result.respond_test_output = test_output
                    if success == True:
                        sample_result.result_type = 'TEST_SUCCESS'
                    else:
                        sample_result.result_type = 'TEST_FAILED'
                    # revert the codex response version to the original fixed version
                    revert_response_to_fixed_version(
                        original_func_lines, args.working_directory, fixed_bug, patch_file_path)
                    save(sample_result)
                else:
                    sample_result.result_type = 'ERROR'
                    sample_result.error_message = str(error)
                    save(sample_result)
        time.sleep(10)
