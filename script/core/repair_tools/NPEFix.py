import os
import subprocess

from core.RepairTool import RepairTool

from config import WORKING_DIRECTORY
from config import Z3_PATH
from config import JAVA8_HOME
from config import JAVA_ARGS
from config import OUTPUT_PATH

class NPEFix(RepairTool):
	"""Nopol"""
	def __init__(self, name="NPEFix"):
		super(Nopol, self).__init__(name, "npefix")
		self.mode = "normal"

	def repair(self, bug):
		bug_path = os.path.join(WORKING_DIRECTORY, "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))
		self.init_bug(bug, bug_path)
		try:
			cmd = """cd %s;
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;
TZ="America/New_York"; export TZ;
export PATH="%s:$PATH";
export JAVA_HOME="%s";
time java %s -cp %s %s \\
	--mode %s \\
	--type %s \\
	--oracle %s \\
	--synthesis %s \\
	--flocal %s \\
	--json \\
	--solver %s \\
	--solver-path %s \\
	--complianceLevel %s \\
	--source %s \\
	--classpath %s;
	echo "\\n\\nNode: `hostname`\\n";
	echo "\\n\\nDate: `date`\\n";
""" % (bug_path,
	JAVA8_HOME,
	JAVA8_HOME,
	JAVA_ARGS, 
	self.jar,
	self.main,
	self.mode,
	self.statement_type,
	self.oracle,
	self.synthesis,
	self.flocal,
	self.solver,
	Z3_PATH,
	str(bug.compliance_level()),
	bug.source_folders(),
	bug.classpath())
			logPath = os.path.join(OUTPUT_PATH, bug.benchmark.name, bug.project, str(bug.bug_id), self.name, str(self.seed), "stdout.log.full")
			if not os.path.exists(os.path.dirname(logPath)):
				os.makedirs(os.path.dirname(logPath))
			log = file(logPath, 'w')
			print(cmd)
			subprocess.call(cmd, shell=True, stdout=log)
			with open(logPath) as data_file:
				return data_file.read()
		finally:
			cmd = "rm -rf %s;" % (bug_path)
			subprocess.call(cmd, shell=True)
		pass