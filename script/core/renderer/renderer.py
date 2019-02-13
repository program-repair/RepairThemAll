import os

from BashRenderer import BashRenderer
from EmptyRenderer import EmptyRenderer


def is_grid5k_node():
    return 'OAR_JOB_ID' in os.environ


def get_renderer(runner):
    """
    :param runner:
    :return: EmptyRenderer
    """
    if is_grid5k_node():
        return EmptyRenderer(runner)
    return BashRenderer(runner)
