from core.repair_tools.Nopol import Nopol


class DynaMoth(Nopol):
    """DynaMoth"""

    def __init__(self, name="DynaMoth", mode="repair", oracle="angelic", statement_type="pre_then_cond", seed=7):
        super(DynaMoth, self).__init__(name, mode, oracle, statement_type, seed)
        self.synthesis = "dynamoth"
