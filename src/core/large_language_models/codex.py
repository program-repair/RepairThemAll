from dotenv import dotenv_values
import openai

config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

EXAMPLE_FILE_PATH = "/Users/pengyu/src/kth/kth-plm-apr/data/example/Fibonacci.java"
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


def main():
    code = repair_code(EXAMPLE_FILE_PATH)
    print(code)


if __name__ == "__main__":
    main()
