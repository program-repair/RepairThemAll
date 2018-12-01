from core.repair_tools.Arja import Arja


def init(args, name, mode):
    return Arja(name=name, mode=mode)


def genprog_init(args):
    return init(args, "GenProg", "GenProg")


def genprog_args(parser):
    parser.set_defaults(func=genprog_init)
    _arja_args(parser)


def kali_init(args):
    return init(args, "Kali", "Kali")


def kali_args(parser):
    parser.set_defaults(func=kali_init)
    _arja_args(parser)


def rsrepair_init(args):
    return init(args, "RSRepair", "RSRepair")


def rsrepair_args(parser):
    parser.set_defaults(func=rsrepair_init)
    _arja_args(parser)


def arja_init(args):
    return init(args, "Arja", "Arja")


def arja_args(parser):
    parser.set_defaults(func=arja_init)
    _arja_args(parser)


def _arja_args(parser):
    parser.add_argument('--version', action='version', version='Arja 4cdec980e8687f32b365843626cc355c07cd754b')
    parser.add_argument("--seed", help="The random seed", default=0, type=float)
    pass
