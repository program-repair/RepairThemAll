import subprocess
import argparse
import sys
import os

from config import REPAIR_ROOT

parser = argparse.ArgumentParser(prog="RepairThemAll", description='RepairThemAll interface')

def run():
    program = None
    if sys.argv[1] == "repair":
        program = "repair.py"
    elif sys.argv[1] == "info":
        program = "info.py"
    elif sys.argv[1] == "checkout":
        program = "checkout.py"
    subprocess.call("python %s %s" % (os.path.join(REPAIR_ROOT, "script", program), program), shell=True)


if __name__ == "__main__":
    run()
