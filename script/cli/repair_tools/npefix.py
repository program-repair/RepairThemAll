from core.repair_tools.NPEFix import NPEFix


def init(args):
    return NPEFix(iteration=args.iteration)


def npefix_args(parser):
    parser.set_defaults(func=init)
    parser.add_argument("--iteration", help="The maximum number of NPEFix iteration", default=100, type=int)
    pass
