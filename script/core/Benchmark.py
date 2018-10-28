
class Benchmark(object):
	"""Benchmark"""
	def __init__(self, name):
		self.name = name
		pass

	def checkout(self, bug, working_directory):
		pass

	def compile(self, bug, working_directory):
		pass

	def run_test(self, bug, working_directory):
		pass

	def classpath(self, bug):
		pass

	def compliance_level(self, bug):
		pass

	def source_folders(self, bug):
		pass

	def test_folders(self, bug):
		pass

	def __str__(self):
		return self.name