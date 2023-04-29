#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
@Author  :   Sen Fang
@Email   :   senf@kth.se
@Ide     :   vscode & conda
@File    :   prompt_config.py
@Time    :   2023/04/01 12:24:14
'''

"""Some ChatGPT prompt candidates."""


PROMPT = {
    'easy': 'Fix the following {} program and return markdown format fixed code.\n\n',
    'advanced': 'I want you to act as an experienced {} developer and your task is debugging and fixing bugs. I will type the wrong {} program and you will fix the bug in the program and return the fixed program. I want you to only reply with the fixed program inside one unique code block, and nothing else. Do not write explanations unless I instruct you to do so.',
    'domain': 'Add domian knowledge', # TODO: Advanced + domain knowledge
}