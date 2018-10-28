import os
import subprocess
import shutil

from config import WORKING_DIRECTORY

from core.repair_tools.Astor import Astor

def run(args):
	bug = args.bug
	tool = Astor(scope=args.scope, seed=args.seed)

	result = tool.repair(bug)
	pass

def astor_args(parser):
    parser.set_defaults(func=run)
    parser.add_argument("--seed", help="The random seed", default=0)
    parser.add_argument("--scope", "-s", help="The scope of the ingredients [local, package, global]", default="local")
    pass

