from core.tools.tokenizer import get_max_completion_size, number_of_tokens, calculate_request_counter


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
    assert 6000 == get_max_completion_size(1.2, 500, 5000)


def test_calculate_request_counter_1():
    # normal
    total_request, n_value, completion_size = calculate_request_counter(
        200, 1.2, 500, 100)
    assert total_request == 7
    assert n_value == 33
    assert completion_size == 120


def test_calculate_request_counter_2():
    total_request, n_value, completion_size = calculate_request_counter(
        200, 1.2, 4000, 3000)
    assert total_request == 200
    assert n_value == 1
    assert completion_size == 3600


def test_calculate_request_counter_3():
    total_request, n_value, completion_size = calculate_request_counter(
        200, 1.2, 4000, 1800)
    assert total_request == 200
    assert n_value == 1
    assert completion_size == 2160


def test_calculate_request_counter_4():
    total_request, n_value, completion_size = calculate_request_counter(
        200, 1.2, 100, 5)
    assert total_request == 1
    assert n_value == 200
    assert completion_size == 6


def test_calculate_request_counter_5():
    total_request, n_value, completion_size = calculate_request_counter(
        1, 1.2, 100, 5)
    assert total_request == 1
    assert n_value == 1
    assert completion_size == 6


def test_calculate_request_counter_6():
    total_request, n_value, completion_size = calculate_request_counter(
        1, 1.2, 5000, 3000)
    assert total_request == 1
    assert n_value == 1
    assert completion_size == 3000
