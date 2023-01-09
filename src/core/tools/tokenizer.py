from math import ceil, floor
from transformers import GPT2TokenizerFast
import os

TOTAL_SAMPLES = 200
MAX_TOKEN_LENGTH = 8000
COMPLETION_RATIO = 1.2
os.environ["TOKENIZERS_PARALLELISM"] = "false"


def number_of_tokens(text):
    if text is None:
        return 0
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    return len(tokenizer(text)['input_ids'])


def get_max_completion_size(prompt_size, bug_size):
    rest = max(int(MAX_TOKEN_LENGTH - prompt_size - bug_size), 0)
    completion_budget = bug_size * COMPLETION_RATIO
    return int(min(rest, completion_budget))


def calculate_request_counter(prompt_size, bug_size):
    completion_size = get_max_completion_size(prompt_size, bug_size)
    n_value = max(floor((MAX_TOKEN_LENGTH - prompt_size) / completion_size), 1)
    total_request = ceil(TOTAL_SAMPLES / n_value)
    return total_request, n_value, completion_size
