import os
from dotenv import dotenv_values
import openai
from core.database.schema import Result
from core.tools.java_lang import get_node_by_hash, load_ast_nodes, load_fixed_code_node
from core.tools.patch import load_patch_file
from core.tools.persist import write_to_file
from core.tools.prompt import generate_prompt
from core.tools.tokenizer import get_max_completion_size, number_of_tokens


config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"
EXAMPLE_BUGGY_FILEPATH = 'data/example/codex_prompt_example_buggy.source'
EXAMPLE_FIXED_FILEPATH = 'data/example/codex_prompt_example_fixed.source'
PROJECT_EXAMPLE_BUGGY_PATH_FORMAT = 'data/example/codex_project_example_{}_buggy.source'
PROJECT_EXAMPLE_FIXED_PATH_FORMAT = 'data/example/codex_project_example_{}_fixed.source'

STOP_SIGN = "###"


def load_buggy_code_node(result, fixed_file_path, buggy_file_path, patch_file_path):
    countable_diffs, result = load_patch_file(result, patch_file_path)
    fixed_node = load_fixed_code_node(
        fixed_file_path, countable_diffs[0].sorted_changes())
    buggy_nodes = load_ast_nodes(buggy_file_path)
    buggy_node = get_node_by_hash(buggy_nodes, fixed_node.hash)
    return fixed_node, buggy_node, result


def request_codex_code_complition(result, code, prompt_size, bug_size):
    max_completion_size = get_max_completion_size(prompt_size, bug_size)
    print('prompt_size: ', prompt_size)
    print('bug_size: ', bug_size)
    print('max_completion_size: ', max_completion_size)
    # https://beta.openai.com/docs/api-reference/completions/create
    print('prompt: ', code)
    request_params = {
        'model': CODEX_MODEL,
        'temperature': 0.8,
        'max_tokens': max_completion_size,
        'top_p': 0.95,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
        'stop': [STOP_SIGN],
    }
    result.request_params = request_params
    response = openai.Completion.create(
        prompt=code,
        model=request_params['model'],
        temperature=request_params['temperature'],
        max_tokens=request_params['max_tokens'],
        top_p=request_params['top_p'],
        frequency_penalty=request_params['frequency_penalty'],
        presence_penalty=request_params['presence_penalty'],
        stop=request_params['stop'],
    )
    print('--->', response)
    return response, result


def repair_code(result, prompt, prompt_size, bug_size, dry_run=False):
    if dry_run:
        print('Dry run, prompt:', prompt)
        return None, result
    else:
        response, result = request_codex_code_complition(
            result, prompt, prompt_size, bug_size)
        return response, result


def apply_response_to_fixed_version(fixed_bug_path, response_text, fixed_node):
    print('fixed_bug_path: ', fixed_bug_path)
    print('fixed_node: ', fixed_node)
    print('response_text: ', response_text)
    try:
        response_text_lines = response_text.split("\n")
        with open(fixed_bug_path, 'r') as file:
            fixed_bug_lines = file.readlines()
        fixed_bug_lines[fixed_node.start_pos -
                        1:fixed_node.end_pos] = response_text_lines
        write_to_file(fixed_bug_path, "\n".join(fixed_bug_lines))
        return True
    except Exception as e:
        print('Error: ', e)
        print('fixed_bug_path: ', fixed_bug_path)
        return False


def fix_bug_by_openai_codex(result: Result, working_directory, bug, patch_file_path, include_document, include_comments, dry_run=False):
    bug_dir = os.path.join(working_directory, "%s_%s_%s" %
                           (bug.benchmark, bug.project, bug.bug_id))
    countable_diffs, result = load_patch_file(result, patch_file_path)
    if len(countable_diffs) > 1:
        print("Skip, more than one file changed")
        return False, result

    # load buggy code
    fixed_bug_path = bug_dir + "_fixed/" + countable_diffs[0].file_path
    buggy_bug_path = bug_dir + "_buggy/" + countable_diffs[0].file_path
    output_file_path = 'output/{}'.format(bug_dir.split('/')[-1])
    project_buggy_path = PROJECT_EXAMPLE_BUGGY_PATH_FORMAT.format(bug.project)
    project_fixed_path = PROJECT_EXAMPLE_FIXED_PATH_FORMAT.format(bug.project)
    print('Fixed bug path: ', fixed_bug_path)
    print('Buggy bug path: ', buggy_bug_path)
    print('output_file_path: ', output_file_path)
    fixed_node, buggy_node, result = load_buggy_code_node(
        result, fixed_bug_path, buggy_bug_path, patch_file_path)

    result.fixed_code_chunk = fixed_node.code_lines_str()
    result.fixed_code_token = number_of_tokens(fixed_node.code_lines_str())

    result.buggy_code_chunk = buggy_node.code_lines_str()
    result.buggy_code_token = number_of_tokens(buggy_node.code_lines_str())

    # should include project specific example
    smallest_bug_example_id = int(bug._get_project_data()['smallestBug'])
    include_project_specific_example = smallest_bug_example_id != 0 and smallest_bug_example_id != int(
        bug.bug_id)

    # generate prompt
    prompt, prompt_size, bug_size = generate_prompt(STOP_SIGN, EXAMPLE_BUGGY_FILEPATH, EXAMPLE_FIXED_FILEPATH,
                                                    project_buggy_path, project_fixed_path, buggy_node, include_document, include_comments, include_project_specific_example)
    write_to_file(output_file_path + '.codex_prompt', prompt)
    response, result = repair_code(
        result, prompt, prompt_size, bug_size, dry_run)

    result.prompt_text = prompt
    result.prompt_size = prompt_size

    # request codex code completion
    # "finish_reason: stop" means the code is fixed
    # "finish_reason: length" means the code is too long
    if response and response.choices[0].finish_reason == 'stop':  # type: ignore
        result.respond_code_chunk = response.choices[0].text  # type: ignore
        result.respond_code_token = number_of_tokens(
            response.choices[0].text)  # type: ignore
        write_to_file(output_file_path + '.codex_response',
                      response.choices[0].text)  # type: ignore
        print(response.choices[0].text)  # type: ignore
        return apply_response_to_fixed_version(fixed_bug_path,
                                               response.choices[0].text, fixed_node), result  # type: ignore

    return False, result
