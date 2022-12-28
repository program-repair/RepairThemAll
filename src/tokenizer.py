from transformers import GPT2TokenizerFast

if __name__ == '__main__':
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    number_of_tokens = len(tokenizer("Hello world")['input_ids'])
    print('number_of_tokens: ', number_of_tokens)
