from core.repair_tools.Nopol import Nopol


def run(args):
    bug = args.bug
    tool = Nopol(seed=args.seed, statement_type=args.statement_type)

    result = tool.repair(bug)
    pass


def nopol_args(parser):
    parser.set_defaults(func=run)
    parser.add_argument("--statement-type", "-t",
                        help="The targeted statement [condition, precondition, pre_then_cond]", default="pre_then_cond")
    parser.add_argument("--seed", "-s", help="The random seed", default=7)
    pass
