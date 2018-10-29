import os
from os.path import expanduser

REPAIR_ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_PATH = os.path.join(REPAIR_ROOT, "data")
REPAIR_TOOL_FOLDER = os.path.join(REPAIR_ROOT, "repair_tools")
WORKING_DIRECTORY = os.path.join("/tmp/")
OUTPUT_PATH = os.path.join(REPAIR_ROOT, "results/")
Z3_PATH = os.path.join(REPAIR_ROOT, "libs", "z3", "z3")
JAVA7_HOME = expanduser("/usr/lib/jvm/java-1.7.0-openjdk-amd64/bin/")
JAVA8_HOME = expanduser("/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin/")
JAVA_ARGS = "-Xmx4048m"
