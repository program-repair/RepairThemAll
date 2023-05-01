import openai
from core.tools.log import printlog
from dotenv import dotenv_values
import os

config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

def request_chatgpt_pr(prompt, request_params, args):
    # https://beta.openai.com/docs/api-reference/completions/create
    # openai.api_key = os.environ.get('OPENAI_API_KEY')
    if args.prompt_level == 'easy':
        response = openai.ChatCompletion.create(
            model=request_params['model'],
            messages=[{"role": "user", "content": prompt}],
            temperature=request_params['temperature'],
            top_p=request_params['top_p'],
            frequency_penalty=request_params['frequency_penalty'],
            presence_penalty=request_params['presence_penalty'],
        )
    elif args.prompt_level == 'advanced':
        response = openai.ChatCompletion.create(
            model=request_params['model'],
            messages=[{'role': 'system', 'content': prompt[0]},
                    {"role": "user", "content": prompt[1]}],
            temperature=request_params['temperature'],
            top_p=request_params['top_p'],
            frequency_penalty=request_params['frequency_penalty'],
            presence_penalty=request_params['presence_penalty'],
        )
    # TODO: add more domain prompt
    printlog('--->', response)
    return response