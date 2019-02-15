import os
import subprocess
import datetime
import json
import shutil
from xml.etree.ElementTree import parse

from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from core.RepairTool import RepairTool
from core.runner.RepairTask import RepairTask
from core.utils import add_repair_tool

class TestInfo(RepairTool):
    """TestInfo"""

    def __init__(self):
        super(TestInfo, self).__init__("TestInfo", "TestInfo")
        self.seed = 0

    def repair(self, repair_task):
        """"
        :type repair_task: RepairTask
        """
        bug = repair_task.bug

        bug_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))
        repair_task.working_directory = bug_path
        self.init_bug(bug, bug_path)

        try:
            bug.run_test()
            reportFiles = []
            for root, dirs, files in os.walk(bug_path):
                for file in files:
                    filePath = os.path.join(root, file)
                    if "target/surefire-reports" in filePath and file.endswith('.xml'):
                        reportFiles.append(filePath)

            passingTests = 0
            failingTests = 0
            erroringTests = 0
            failureDetails = []
            for xmlFile in reportFiles:
                with open(xmlFile, 'r') as file:
                    xmlTree = parse(file)
                    testCases = xmlTree.findall('testcase')
                    for testCase in testCases:
                        failureDetail = {}
                        failureDetail['testClass'] = testCase.attrib['classname']
                        failureDetail['testMethod'] = testCase.attrib['name']
                        
                        failure = testCase.findall('failure')
                        if len(failure) > 0:
                            failingTests += 1
                            failureDetail['failureName'] = failure[0].attrib['type']
                            if 'message' in failure[0].attrib:
                                failureDetail['detail'] = failure[0].attrib['message']
                            failureDetail['isError'] = False
                            failureDetails.append(failureDetail)
                        else:
                            error = testCase.findall('error')
                            if len(error) > 0:
                                erroringTests += 1
                                failureDetail['failureName'] = error[0].attrib['type']
                                if 'message' in error[0].attrib:
                                    failureDetail['detail'] = error[0].attrib['message']
                                failureDetail['isError'] = True
                                failureDetails.append(failureDetail)
                            else:
                                passingTests += 1

            jsonFile = {
                'failing_tests':  bug.failing_tests(),
                'sources': bug.source_folders(),
                'tests': bug.test_folders(),
                'bin_folders': bug.bin_folders(),
                'test_bin_folders': bug.test_bin_folders(),
                'classpath': bug.classpath(),
                'compliance_level': bug.compliance_level()
            }
            jsonFile['benchmark'] = bug.benchmark.name
            jsonFile['bugId'] = bug.bug_id

            repository = {}
            repository['name'] = bug.project
            jsonFile['repository'] = repository

            try:
                projectInfo = bug.benchmark._get_project_info(bug)
                jsonFile['projectInfo'] = projectInfo
                projectMetrics = {}
                if projectInfo is not None:
                    projectMetrics['numberModules'] = len(projectInfo['modules'])
                jsonFile['projectMetrics'] = projectMetrics
            except:
                pass
                
            tests = {}
            overallMetrics = {}
            overallMetrics['numberPassing'] = passingTests
            overallMetrics['numberRunning'] = passingTests + failingTests + erroringTests
            overallMetrics['numberFailing'] = failingTests
            overallMetrics['numberErroring'] = erroringTests
            tests['overallMetrics'] = overallMetrics
            tests['failureDetails'] = failureDetails
            jsonFile['tests'] = tests


            test_results_path = os.path.join(OUTPUT_PATH, 'testResults', bug.benchmark.name)
            if not os.path.exists(test_results_path):
                os.makedirs(test_results_path)
            

            bug_id = "%s_%s" % (bug.project, bug.bug_id)
            surefire_path = os.path.join(OUTPUT_PATH, 'surefire', bug.benchmark.name, bug_id)
            if not os.path.exists(surefire_path):
                os.makedirs(surefire_path)
            
            for f in reportFiles:
                shutil.copy(f, os.path.join(surefire_path, os.path.basename(f)))
            
            if os.path.exists(os.path.join(WORKING_DIRECTORY, "all-tests.txt")):
                shutil.copy(os.path.join(WORKING_DIRECTORY, "all-tests.txt"), os.path.join(surefire_path, "all-tests.txt"))
            if os.path.exists(os.path.join(WORKING_DIRECTORY, "failing_tests")):
                shutil.copy(os.path.join(WORKING_DIRECTORY, "failing_tests"), os.path.join(surefire_path, "failing_tests"))

            with open(os.path.join(test_results_path, bug_id + '.json'), 'w') as f:
                f.write(json.dumps(jsonFile, indent=2))
        finally:
            cmd = "rm -rf %s;" % (bug_path)
            subprocess.call(cmd, shell=True)
        pass

def init_TestInfo(args):
    return TestInfo()

add_repair_tool("TestInfo", init_TestInfo, 'Repair the bug with TestInfo')