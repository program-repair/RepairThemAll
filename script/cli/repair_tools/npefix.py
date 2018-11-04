from core.repair_tools.NPEFix import NPEFix


def init(args):
    return NPEFix()


def npefix_args(parser):
    parser.set_defaults(func=init)
    pass
