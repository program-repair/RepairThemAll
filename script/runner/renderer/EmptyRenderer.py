from runner.Runner import Runner


class EmptyRenderer(object):
    def __init__(self, runner):
        """
        :param runner:
        :type runner: Runner
        """
        self.runner = runner
        pass

    def render(self):
        pass

    def render_final_result(self):
        pass
