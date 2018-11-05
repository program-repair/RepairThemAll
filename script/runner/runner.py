from local.LocalRunner import LocalRunner


def get_runner(tasks):
    """
    :param tasks:
    :return: Runner
    """
    return LocalRunner(tasks)
