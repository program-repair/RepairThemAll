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
    'easy': 'Fix the following {} program and return markdown format fixed code.\n\n',
    'advanced': 'The following {} program has a bug, I need you to fix it and return markdown format fixed code.\n\n',
    'actor': 'Now you are a developer and you are proficient in {} programming language. You are assigned to fix the following Java program. The fixed Java program you return needs to satisfy the following three points: 1) The returned Java program must be in markdown format; 2) The code should not contain any comment; 3) The code must be compilable.\n\n',
    'domain': 'Now you are a developer and you proficient in {} programming language. You are assigned to fix the following bug. You need to return markdown format fixed code. Your generated fixed code must pass the following unit test.',
}
