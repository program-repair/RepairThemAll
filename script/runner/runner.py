import os

from local.LocalRunner import LocalRunner
from grid5k.Grid5kRunner import Grid5kRunner


def is_grid5k():
    return os.path.exists("/usr/bin/oarsub")


def get_runner(tasks, args):
    """
    :param tasks:
    :return: Runner
    """
    if is_grid5k():
        return Grid5kRunner(tasks, args)
    return LocalRunner(tasks, args)
