from dotenv import dotenv_values
import openai
import javalang
import whatthepatch
import pprint
import re

config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

EXAMPLE_FILE_PATH = "/Users/pengyu/src/kth/plm-repair-them-all/data/example/Fibonacci.java"
EXAMPLE_PATCH_FILE_PATH = "/Users/pengyu/src/kth/plm-repair-them-all/benchmarks/defects4j/framework/projects/Chart/patches/19.src.patch"
MAX_TOKEN_LENGTH = 8000
CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"


def clean_code(lines):
    # remove right side trailing space
    lines = [line.rstrip() for line in lines]
    # remove empty lines
    lines = [x for x in lines if x]
    return '\n'.join(lines)


def prepare_buggy_code(file_path):
    # read file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # clean code
    return clean_code(lines)


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


def load_file_as_ast(file_path):
    pp = pprint.PrettyPrinter(indent=4)
    with open(file_path, 'r') as file:
        text = file.read()
        tree = javalang.parse.parse(text)
    nodes = filter_ast_nodes_by_types(
        tree, ['MethodDeclaration', 'ClassDeclaration'])

    for node in nodes:
        pp.pprint(node.name)


def filter_ast_nodes_by_types(root, node_types):
    filtered_nodes = []
    for node in root:
        if isinstance(node, tuple):
            for t in node:
                if not isinstance(t, tuple):
                    if t.__class__.__name__ in node_types:
                        filtered_nodes.append(t)
        else:
            if node.__class__.__name__ in node_types:
                filtered_nodes.append(node)

    return filtered_nodes


def is_line_countable(line):
    striped_line = line.strip()
    isComment = re.match(r'^(//|/\*|\*|\*/)', striped_line)
    hasMultiChars = len(striped_line) > 1
    return not isComment and hasMultiChars


def load_patch_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    for diff in whatthepatch.parse_patch(text):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint('diff--------------------------------------------------------')
        pp.pprint(diff.header)
        pp.pprint(diff.text)
        countable_changes = []
        for change in diff.changes or []:
            if change.new == None and is_line_countable(change.line):
                countable_changes.append(change)
        pp.pprint(countable_changes)


def main():
    code = repair_code(EXAMPLE_FILE_PATH)
    print(code)


if __name__ == "__main__":
    # main()
    load_file_as_ast(EXAMPLE_FILE_PATH)
    # load_patch_file((EXAMPLE_PATCH_FILE_PATH))
