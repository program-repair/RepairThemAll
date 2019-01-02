from core.repair_tools.Astor import Astor


def init(args, name, mode):
    return Astor(name=name,
                    mode=mode,
                    maxgen=args.maxgen,
                    max_time=args.maxtime,
                    population=args.population,
                    scope=args.scope,
                    parameters=args.parameters,
                    seed=args.seed)


def cardumen_init(args):
    args.parameters += ":maxCombinationVariableLimit:true:maxVarCombination:1000"
    return init(args, "Cardumen", "cardumen")

def cardumen_args(parser):
    parser.set_defaults(func=cardumen_init)
    astor_args(parser)

def jgenprog_init(args):
    return init(args, "jGenProg", "jgenprog")


def jgenprog_args(parser):
    parser.set_defaults(func=jgenprog_init)
    astor_args(parser)

def jkali_init(args):
    return init(args, "jKali", "jkali")


def jkali_args(parser):
    parser.set_defaults(func=jkali_init)
    astor_args(parser)

def jMutRepair_init(args):
    return init(args, "jMutRepair", "jMutRepair")


def jMutRepair_args(parser):
    parser.set_defaults(func=jMutRepair_init)
    astor_args(parser)


def astor_args(parser):
    parser.add_argument("--seed", help="The random seed", default=0, type=float)
    parser.add_argument("--maxtime", help="Astor timeout", default=120, type=int)
    parser.add_argument("--population", help="Astor population", default=1, type=int)
    parser.add_argument("--maxgen", help="Astor maxgen", default=1000000, type=int)
    parser.add_argument("--scope", "-s", help="The scope of the ingredients", choices=("local", "package", "global"),
                        default="local")
    parser.add_argument("--parameters", "-p", help="Astor parameters", default="x:x")
    parser.add_argument("--dontstopfirst", help="Don't stop after the first bug",
                        action='store_false',
                        dest='stopfirst',
                        default=True)
    parser.add_argument('--version', action='version', version='Astor 26ee3dfc8b2d7ed4373f7cfe0d4bd5bcf31d9f28')
    pass
