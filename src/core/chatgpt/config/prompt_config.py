#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
@Author  :   Sen Fang
@Email   :   senf@kth.se
@Ide     :   vscode & conda
@File    :   prompt_config.py
@Time    :   2023/04/01 12:24:14
'''

"""Some configurations for ChatGPT prompt."""


PROMPT = {
    'easy': 'Fix the following {} program and return markdown style fixed code.\n',
    'advanced': 'The following {} program has a bug, I need you to fix it and return markdown style fixed code.\n',
    'actor': 'Now you are a developer and you proficient in {} programming language. You are assigned to fix the following bug. You need to return markdown style fixed code.\n',
    'domain': 'Now you are a developer and you proficient in {} programming language. You are assigned to fix the following bug. You need to return markdown style fixed code. Your generated fixed code must pass the following unit test.',
}
