import os
from dotenv import dotenv_values
from os.path import expanduser

env_config = dotenv_values(".env")

REPAIR_ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_PATH = os.path.join(REPAIR_ROOT, "data")
REPAIR_TOOL_FOLDER = os.path.join(REPAIR_ROOT, "repair_tools")
WORKING_DIRECTORY = os.environ.get(
    "WORKING_DIRECTORY", expanduser("/repair/"))
OUTPUT_PATH = os.environ.get(
    "OUTPUT_PATH", expanduser("/repair/results"))

Z3_PATH = os.path.join(REPAIR_ROOT, "libs", "z3", "build")

MAVEN_BIN = os.environ.get("MAVEN_BIN", expanduser(
    "/repair/deps/Maven/apache-maven/bin/"))

JAVA7_HOME = os.environ.get(
    "JAVA7_HOME", expanduser("/Library/Java/JavaVirtualMachines/zulu-7.jdk/Contents/Home/bin"))
JAVA8_HOME = env_config.get('JAVA8_HOME')
JAVA_ARGS = os.environ.get("JAVA_ARGS", "-Xmx4g -Xms1g")

LOCAL_THREAD = int(os.environ.get("THREADS", "1"))
GRID5K_MAX_NODE = 50
# In minutes
TOOL_TIMEOUT = os.environ.get("TOOL_TIMEOUT", "120")
# Format: HH:MM ## the fuction getGridTime calculates the timeout of the grid taking into account an overhead (expressed as percentage)
# GRID5K_TIME_OUT = getGridTime(TOOL_TIMEOUT, overhead=0.33)
