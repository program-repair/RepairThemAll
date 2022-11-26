from dotenv import dotenv_values
import openai
import whatthepatch
import pprint
import lang_utils

config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

EXAMPLE_FILE_PATH = "/Users/pengyu/src/kth/plm-repair-them-all/data/example/Fibonacci.java"
EXAMPLE_BUGGY_FILE_PATH = "/Users/pengyu/src/kth/repair/Defects4J_Closure_3/src/com/google/javascript/jscomp/FlowSensitiveInlineVariables.java"
EXAMPLE_PATCH_FILE_PATH = "/Users/pengyu/src/kth/plm-repair-them-all/benchmarks/defects4j/framework/projects/Closure/patches/3.src.patch"
MAX_TOKEN_LENGTH = 8000
CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"


def prepare_buggy_code(file_path):
    # read file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # clean code
    return lang_utils.clean_code(lines)


def add_prompt_to_code(code):
    return "##### Fix bugs in the below function\n \n### Buggy Java\n" + code + "\n### Fixed Java\n"


def request_codex_code_complition(code):
    # https://beta.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model=CODEX_MODEL,
        prompt=code,
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###"]
    )
    return response.choices[0].text  # type: ignore


def repair_code(file_path):
    code = prepare_buggy_code(file_path)
    # add prompt
    code = add_prompt_to_code(code)
    token_length = len(code.split())

    if token_length > MAX_TOKEN_LENGTH:
        print(CODE_TOO_LONG)
        return
    else:
        print('token length: ', token_length)
        response = request_codex_code_complition(code)
        return response


def load_patch_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    for diff in whatthepatch.parse_patch(text):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(diff.header)
        pp.pprint(diff.text)
        countable_changes = []
        for change in diff.changes or []:
            if change.new == None and lang_utils.is_line_countable(change.line):
                countable_changes.append(change)
        pp.pprint(countable_changes)


def main():
    code = repair_code(EXAMPLE_FILE_PATH)
    print(code)


if __name__ == "__main__":
    # main()
    load_patch_file(EXAMPLE_PATCH_FILE_PATH)
    print('--------------------------------------------------------')
    method_nodes = lang_utils.parse_method_metainfo(EXAMPLE_BUGGY_FILE_PATH)
    for mn in method_nodes:
        print(mn)
