import os
import subprocess
import shutil

from config import WORKING_DIRECTORY

from core.repair_tools.NPEFix import NPEFix

def run(args):
	bug = args.bug
	tool = NPEFix()

	result = tool.repair(bug)
	pass

def npefix_args(parser):
    parser.set_defaults(func=run)
    pass

