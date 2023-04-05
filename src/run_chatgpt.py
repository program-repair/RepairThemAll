#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
@Author  :   Sen Fang
@Email   :   senf@kth.se
@Ide     :   vscode & conda
@File    :   run_chatgpt.py
@Time    :   2023/04/01 11:52:36
'''

"""This code is derived from ask_defects4j.py and can request ChatGPT and its improved version for program repair."""

import argparse
import time
from core.chatgpt.config.defs4j_config import AttrDict
from core.chatgpt.config.prompt_config import PROMPT
from core.chatgpt.request_chatgpt import ask_chatgpt


def main():
    parser = argparse.ArgumentParser(
        prog="ask", description='Checkout and fix the bug by chatable large language model')
    parser.add_argument("--model", "-m", required=True, choices=["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"],
                        help="The chatable LLMs you want to use.")
    parser.add_argument("--benchmark", "-b", required=True, default="Defects4J",
                        help="The benchmark to repair.")
    parser.add_argument("--project", "-p", required=False,
                        help="The project name (case sensitive).")
    parser.add_argument("--id", "-i", required=False, help="The bug id")
    parser.add_argument("--start", "-s", required=False,
                        help="The bug id starts from")
    parser.add_argument("--working_directory", "-w",
                        required=True, help="The working directory")
    parser.add_argument("--num_samples", "-ns", type=int, default=10, help="The number of samples to generate.")
    parser.add_argument("--num_requests", "-nr", type=int, default=10, help="The number of requests to generate.")
    parser.add_argument("--temperature", "-t", type=float, default=0.8, help="The temperature used to generate the patch.")
    parser.add_argument("--max_tokens", "-mt", type=int, default=2048, help="The max tokens used to generate the patch.")
    parser.add_argument("--top_p", "-tp", type=float, default=0.95, help="The top_p used to generate the patch.")
    parser.add_argument("--presence_penalty", "-pp", type=float, default=0.0, help="The presence_penalty used to generate the patch.")
    parser.add_argument("--frequency_penalty", "-fp", type=float, default=0.0, help="The frequency_penalty used to generate the patch.")
    parser.add_argument("--prompt_level", "-pml", type=str, default="easy", choices=["easy", "adavanced", "actor", "domain"], help="The prompt used to generate the patch.")
    parser.add_argument("--prompt", "-pm", type=str, default=None, help="The prompt used to generate the patch.")
    parser.add_argument("--pl", "-pl", type=str, default="java", help="The programming language want to fix.")

    args = parser.parse_args()
    defects4j_config = AttrDict()
    fixa_config = defects4j_config.fixa_config
    defects4j_projects = defects4j_config.defects4j_projects
    defects4j_bug_size = defects4j_config.defects4j_bug_size
    defects4j_config.benchmark = args.benchmark
    if args.project != None:
        defects4j_config.project = args.project
    defects4j_config.bug_id = args.id
    defects4j_config.model = args.model
    assert args.project in defects4j_projects or args.project == None, "The project name is not valid, please check!"
    
    if args.prompt == None:
        args.prompt = PROMPT[args.prompt_level].format(args.pl)
    
    fixa_config['sample'] = args.num_samples

    if args.project != None and args.id != None:
        # fix a single bug
        ask_chatgpt(args, args.id, defects4j_config, fixa_config)

    elif args.project != None and args.id == None:
        # fix all bugs in a project
        bug_size = defects4j_bug_size[args.project]
        starts_from = int(args.start) if args.start != None else 1
        for bug_id in range(starts_from, bug_size + 1):
            defects4j_config.bug_id = args.id
            ask_chatgpt(args, str(bug_id), defects4j_config, fixa_config)
            time.sleep(12)
    else:
        # fix all bugs from all projects
        for project, bug_size in defects4j_bug_size.items():
            defects4j_config.project = project
            for bug_id in range(1, bug_size + 1):
                defects4j_config.bug_id = args.id
                ask_chatgpt(args, str(bug_id), defects4j_config, fixa_config)
                time.sleep(12)


if __name__ == "__main__":
    main()
 
    # elif args.project == None and args.id == None:
    #     # fix all bugs from all projects
    #     for project, bug_size in DEFECTS4J_BUG_SIZE.items():
    #         args.project = project
    #         for bug_id in range(1, bug_size + 1):
    #             ask_codex_for_single_bug(args, str(bug_id), FIXA_CONFIG)
    #             time.sleep(12)
    # else:
    #     ask_codex_for_single_bug(args, args.id, FIXA_CONFIG)
