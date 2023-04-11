#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
@Author  :   Sen Fang
@Email   :   senf@kth.se
@Ide     :   vscode & conda
@File    :   config.py
@Time    :   2023/04/01 11:58:00
'''

"""The configurations dict for Defects4J benchmark."""


class AttrDict(dict):
    """A dict that allows for attribute-style access."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
        self.id: int = None
        self.model: str = None
        self.benchmark: str = None
        self.project: str = None
        self.bug_id: int = None
        self.request_type: str = None
        self.sample_number: int = None
        self.prompt_text: str = None
        self.prompt_size: int = None
        self.bug_start_pos: int = None
        self.bug_end_pos: int = None
        self.temperature: float = None
        self.buggy_file_path: str = None
        self.patch: str = None
        self.buggy_code_chunk: str = None
        self.buggy_code_token: int = None
        self.fixed_code_chunk: str = None
        self.fixed_code_token: int = None
        self.respond_origin_code_chunk: str = None
        self.respond_clean_code_chunk: str = None
        self.respond_original_text: dict = {}
        self.respond_code_token: dict = {}
        self.respond_compiled_output: str = None
        self.respond_test_output: str = None
        self.respond_type: str = None
        self.buggy_test_output: str = None
        self.fixed_test_output: str = None
        self.prompt_params: dict = None
        self.request_params: dict = None
        self.result_type: dict = {}
        self.error_message: str = None
        self.defects4j_bug_size: dict = {
                                            'Chart': 26,
                                            'Cli': 40,
                                            'Closure': 176,
                                            'Codec': 18,
                                            'Collections': 28,
                                            'Compress': 47,
                                            'Csv': 16,
                                            'Gson': 18,
                                            'JacksonCore': 26,
                                            'JacksonDatabind': 112,
                                            'JacksonXml': 6,
                                            'Jsoup': 93,
                                            'JxPath': 22,
                                            'Lang': 65,
                                            'Math': 106,
                                            'Mockito': 38,
                                            'Time': 27,
                                        }
        self.fixa_config: dict = {
                                    'include_document': False,
                                    'include_comments': False,
                                    'compile': True,
                                    'sample': None,
                                    'completion_ratio': 1.2,
                                 }
        self.defects4j_projects: list = ['Chart', 'Cli', 'Closure', 'Codec', 'Collections', 'Compress', 'Csv', 'Gson',
                                         'JacksonCore', 'JacksonDatabind', 'JacksonXml', 'Jsoup', 'JxPath', 'Lang', 'Math', 'Mockito', 'Time']
