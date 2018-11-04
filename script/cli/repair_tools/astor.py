from core.repair_tools.Astor import Astor


def init(args):
    return Astor(scope=args.scope, seed=args.seed)


def astor_args(parser):
    parser.set_defaults(func=init)
    parser.add_argument("--seed", help="The random seed", default=0, type=float)
    parser.add_argument("--scope", "-s", help="The scope of the ingredients", choices=("local", "package", "global"), default="local")
    parser.add_argument("--dontstopfirst", help="Don't stop after the first bug",
                        action='store_false',
                        dest='stopfirst',
                        default=True)
    parser.add_argument('--version', action='version', version='Astor 61e33ecf2be00a5f03d06e49659ddfde7bcc1431')
    pass
