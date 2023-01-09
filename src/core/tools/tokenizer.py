from math import ceil, floor
from transformers import GPT2TokenizerFast
import os

MAX_TOKEN_LENGTH = 8000
MAX_COMPLETION_TOKEN_LENGTH = 4000
completion_ratio = 1.2
os.environ["TOKENIZERS_PARALLELISM"] = "false"


def number_of_tokens(text):
    if text is None:
        return 0
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    return len(tokenizer(text)['input_ids'])


def get_max_completion_size(completion_ratio, prompt_size, bug_size):
    rest = max(int(MAX_TOKEN_LENGTH - prompt_size - bug_size), 0)
    completion_budget = bug_size * completion_ratio
    return int(min(rest, completion_budget))


def calculate_request_counter(total_samples, completion_ratio, prompt_size, bug_size):
    completion_size = get_max_completion_size(
        completion_ratio, prompt_size, bug_size)
    n_value = max(floor(MAX_COMPLETION_TOKEN_LENGTH / completion_size), 1)
    total_request = ceil(total_samples / n_value)
    return total_request, n_value, completion_size
