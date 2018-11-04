from core.repair_tools.Nopol import Nopol


def init(args):
    return Nopol(name="DynaMoth", seed=args.seed, statement_type=args.statement_type, synthesis="dynamoth")


def dynamoth_args(parser):
    parser.set_defaults(func=init)
    parser.add_argument("--statement-type", "-t",
                        help="The targeted statement", default="pre_then_cond", choices=("condition", "precondition", "pre_then_cond"))
    parser.add_argument("--seed", "-s", help="The random seed", default=7)
    pass
