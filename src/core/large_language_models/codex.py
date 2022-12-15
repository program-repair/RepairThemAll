from dotenv import dotenv_values
import openai
import nltk
from core.tools.java_lang import get_node_by_hash, load_ast_nodes, load_fixed_code_node
from core.tools.patch import load_patch_file
from core.tools.persist import log4output
from core.tools.prompt import generate_prompt


nltk.download('punkt')

config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

MAX_TOKEN_LENGTH = 3570
CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"
EXAMPLE_BUGGY_FILEPATH = 'data/example/codex_prompt_example_buggy.source'
EXAMPLE_FIXED_FILEPATH = 'data/example/codex_prompt_example_fixed.source'

STOP_SIGN = "###"


def load_buggy_code_node(fixed_file_path, buggy_file_path, patch_file_path):
    countable_diffs = load_patch_file(patch_file_path)
    fixed_node = load_fixed_code_node(
        fixed_file_path, countable_diffs[0].sorted_changes())
    buggy_nodes = load_ast_nodes(buggy_file_path)
    buggy_node = get_node_by_hash(buggy_nodes, fixed_node.hash)
    return buggy_node


def request_codex_code_complition(code):
    # https://beta.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model=CODEX_MODEL,
        prompt=code,
        temperature=0.8,
        max_tokens=MAX_TOKEN_LENGTH,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[STOP_SIGN]
    )
    # return response.choices[0].text  # type: ignore
    return response


def repair_code(prompt, dry_run=False):
    token_length = len(nltk.word_tokenize(prompt))

    if token_length > MAX_TOKEN_LENGTH:
        print(CODE_TOO_LONG)
        return
    elif dry_run:
        print('Dry run, prompt:', prompt)
        return
    else:
        response = request_codex_code_complition(prompt)
        return response


def fix_bug_by_openai_codex(bug_dir, patch_file_path, dry_run=False):
    countable_diffs = load_patch_file(patch_file_path)
    if len(countable_diffs) == 1:
        fixed_bug_path = bug_dir + "_fixed/" + countable_diffs[0].file_path
        buggy_bug_path = bug_dir + "_buggy/" + countable_diffs[0].file_path
        output_file_path = 'output/{}'.format(bug_dir.split('/')[-1])
        print('Fixed bug path: ', fixed_bug_path)
        print('Buggy bug path: ', buggy_bug_path)
        print('output_file_path: ', output_file_path)
        buggy_node = load_buggy_code_node(
            fixed_bug_path, buggy_bug_path, patch_file_path)
        prompt = generate_prompt(
            STOP_SIGN, EXAMPLE_BUGGY_FILEPATH, EXAMPLE_FIXED_FILEPATH, buggy_node)
        log4output(output_file_path + '.prompt', prompt)
        response = repair_code(prompt, dry_run)
        if response:
            log4output(output_file_path + '.response',
                       response.choices[0].text)
            print(response.choices[0].text)  # type: ignore
        return response
    else:
        print("Skip, more than one file changed")
        return
