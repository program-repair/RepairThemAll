import os
from dotenv import dotenv_values
import openai
import nltk
from core.tools.java_lang import get_node_by_hash, load_ast_nodes, load_fixed_code_node
from core.tools.patch import load_patch_file
from core.tools.persist import write_to_file
from core.tools.prompt import generate_prompt


nltk.download('punkt')

config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

MAX_TOKEN_LENGTH = 3570
CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"
EXAMPLE_BUGGY_FILEPATH = 'data/example/codex_prompt_example_buggy.source'
EXAMPLE_FIXED_FILEPATH = 'data/example/codex_prompt_example_fixed.source'
PROJECT_EXAMPLE_BUGGY_PATH_FORMAT = 'data/example/codex_project_example_{}_buggy.source'
PROJECT_EXAMPLE_FIXED_PATH_FORMAT = 'data/example/codex_project_example_{}_fixed.source'

STOP_SIGN = "###"


def load_buggy_code_node(fixed_file_path, buggy_file_path, patch_file_path):
    countable_diffs = load_patch_file(patch_file_path)
    fixed_node = load_fixed_code_node(
        fixed_file_path, countable_diffs[0].sorted_changes())
    buggy_nodes = load_ast_nodes(buggy_file_path)
    buggy_node = get_node_by_hash(buggy_nodes, fixed_node.hash)
    return fixed_node, buggy_node


def request_codex_code_complition(code):
    # https://beta.openai.com/docs/api-reference/completions/create
    print('prompt: ', code)
    response = openai.Completion.create(
        model=CODEX_MODEL,
        prompt=code,
        temperature=0.2,
        max_tokens=MAX_TOKEN_LENGTH,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[STOP_SIGN],
    )
    print('--->', response)
    # return response.choices[0].text  # type: ignore
    return response


def repair_code(prompt, dry_run=False):
    # TODO: comment out for now, need to move to the place after generating prompt
    # token_length = len(nltk.word_tokenize(prompt))
    # if token_length > MAX_TOKEN_LENGTH:
    #    print(CODE_TOO_LONG)
    #    return

    if dry_run:
        print('Dry run, prompt:', prompt)
        return
    else:
        response = request_codex_code_complition(prompt)
        return response


def apply_response_to_fixed_version(fixed_bug_path, response_text, fixed_node):
    response_text_lines = response_text.split("\n")
    with open(fixed_bug_path, 'r') as file:
        fixed_bug_lines = file.readlines()
    fixed_bug_lines[fixed_node.start_line -
                    1:fixed_node.end_line] = response_text_lines
    write_to_file(fixed_bug_path, "\n".join(fixed_bug_lines))


def fix_bug_by_openai_codex(working_directory, bug, patch_file_path, include_document, include_comments, dry_run=False):
    bug_dir = os.path.join(working_directory, "%s_%s_%s" %
                           (bug.benchmark, bug.project, bug.bug_id))
    countable_diffs = load_patch_file(patch_file_path)
    if len(countable_diffs) > 1:
        print("Skip, more than one file changed")
        return

    # load buggy code
    fixed_bug_path = bug_dir + "_fixed/" + countable_diffs[0].file_path
    buggy_bug_path = bug_dir + "_buggy/" + countable_diffs[0].file_path
    output_file_path = 'output/{}'.format(bug_dir.split('/')[-1])
    project_buggy_path = PROJECT_EXAMPLE_BUGGY_PATH_FORMAT.format(bug.project)
    project_fixed_path = PROJECT_EXAMPLE_FIXED_PATH_FORMAT.format(bug.project)
    print('Fixed bug path: ', fixed_bug_path)
    print('Buggy bug path: ', buggy_bug_path)
    print('output_file_path: ', output_file_path)
    fixed_node, buggy_node = load_buggy_code_node(
        fixed_bug_path, buggy_bug_path, patch_file_path)

    # should include project specific example
    smallest_bug_example_id = int(bug._get_project_data()['smallestBug'])
    include_project_specific_example = smallest_bug_example_id != 0 and smallest_bug_example_id != int(
        bug.bug_id)

    # generate prompt
    prompt = generate_prompt(STOP_SIGN, EXAMPLE_BUGGY_FILEPATH, EXAMPLE_FIXED_FILEPATH,
                             project_buggy_path, project_fixed_path, buggy_node, include_document, include_comments, include_project_specific_example)
    write_to_file(output_file_path + '.codex_prompt', prompt)
    response = repair_code(prompt, dry_run)

    # request codex code completion
    # "finish_reason: stop" means the code is fixed
    # "finish_reason: length" means the code is too long
    if response and response.choices[0].finish_reason == 'stop':
        write_to_file(output_file_path + '.codex_response',
                      response.choices[0].text)  # type: ignore
        print(response.choices[0].text)  # type: ignore
        apply_response_to_fixed_version(
            fixed_bug_path, response.choices[0].text, fixed_node)  # type: ignore
        return True
    return False
