from runner.local.LocalRunner import LocalRunner


def get_runner(tasks):
    return LocalRunner(tasks)