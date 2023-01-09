from core.tools.tokenizer import get_max_completion_size, number_of_tokens


def test_number_of_tokens_text():
    result = number_of_tokens("Hello world")
    assert result == 2


def test_number_of_tokens_example():
    example_fixed_filepath = 'data/example/codex_prompt_example_fixed.source'
    with open(example_fixed_filepath, 'r') as file:
        first_fixed_example_lines = file.readlines()
    first_fixed_example = "".join(first_fixed_example_lines)
    result = number_of_tokens(first_fixed_example)
    assert result == 190


def test_get_max_completion_size():
    assert 120 == get_max_completion_size(1.2, 500, 100)
    assert 1200 == get_max_completion_size(1.2, 500, 1000)
    assert 2500 == get_max_completion_size(1.2, 500, 5000)
