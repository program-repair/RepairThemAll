import os
import shutil
import time
from dotenv import dotenv_values
import openai
from core.tools.log import printlog
from core.tools.persist import write_to_file
from core.utils import get_benchmark


config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')


def apply_text_to_buggy_version(buggy_bug_path, defects4j_config):
    try:
        response_text_lines = defects4j_config["respond_code_chunk"].split("\n")
        with open(buggy_bug_path, 'r') as file:
            buggy_bug_lines = file.readlines()
        new_buggy_bug_file = "".join(buggy_bug_lines[0:defects4j_config["bug_start_pos"] - 1]) + \
            "\n".join(response_text_lines) + \
            "".join(buggy_bug_lines[defects4j_config["bug_end_pos"]:])
        write_to_file(buggy_bug_path, new_buggy_bug_file)
        return True, None
    except Exception as e:
        printlog('Error: ', e)
        printlog('buggy_bug_path: ', buggy_bug_path)
        return False, e


# revert fixed bug file after testing codex response
def revert_response_to_buggy_version(bug_dir, benchmark, working_directory, project, bug_id):
    printlog('revert buggy bug file after testing chatgpt response')
    buggy_path = bug_dir + "_buggy/"
    printlog('clean buggy_bug_path: ', buggy_path)
    shutil.rmtree(buggy_path)
    buggy_bug = checkout_bug(
        benchmark, working_directory, project, bug_id, 'buggy')
    buggy_bug.compile()


def checkout_bug(benchmark, working_directory, project, bug_id, version):
    bug_identifier = project + '_' + str(bug_id)

    bug_path = os.path.join(working_directory,
                            "%s_%s_%s_%s" % (benchmark.name, project, str(bug_id), version))

    printlog('bug_identifier: ', bug_identifier)
    bug = benchmark.get_bug(bug_identifier)
    printlog('bug: ', bug)
    is_buggy_version = version == 'buggy'
    bug.checkout(bug_path, is_buggy_version)

    return bug


def checkout_buggy_version(benchmark, working_directory, project, bug_id):
    try:
        # checkout buggy bug
        buggy_bug = checkout_bug(
            benchmark, working_directory, project, bug_id, 'buggy')
        return buggy_bug
    except Exception as e:
        printlog(
            'Something went wrong when checkout buggy version of bug {} {}-------\n'.format(project, bug_id), e)
        return None


def verify_response(defects4j_config, buggy_bug_path, buggy_bug, sample_number):
    if defects4j_config["respond_type"] == 'RESPONDED' or defects4j_config["respond_type"] == 'SAMPLE_ERROR':
        # apply the choice to the code
        applied, error = apply_text_to_buggy_version(buggy_bug_path, defects4j_config)
        if applied:
            defects4j_config["result_type"][str(sample_number)] = 'APPLIED'
            compiled_output = buggy_bug.compile()
            defects4j_config["respond_compiled_output"] = compiled_output
            if compiled_output.count('OK') == 2:
                defects4j_config["result_type"][str(sample_number)] = 'COMPILED_SUCCESS'
                # only run test if the code is compiled successfully
                success, test_output = buggy_bug.run_test()
                printlog('test_output: \n', test_output)
                defects4j_config["respond_test_output"] = test_output
                if success == True:
                    defects4j_config["result_type"][str(sample_number)] = 'TEST_SUCCESS'
                elif defects4j_config["respond_test_output"].count('OK') < 2 and defects4j_config["respond_test_output"].count('Failing tests:') == 0:
                    defects4j_config["result_type"][str(sample_number)] = 'TEST_TIMEOUT'
                elif len(defects4j_config["respond_test_output"]) < len(defects4j_config["buggy_test_output"]) and defects4j_config["respond_test_output"] == defects4j_config["fixed_test_output"]:
                    defects4j_config["result_type"][str(sample_number)] = 'TEST_FAILED_BUT_MATCHED_REDUCED'
                elif len(defects4j_config["respond_test_output"]) < len(defects4j_config["buggy_test_output"]):
                    defects4j_config["result_type"][str(sample_number)] = 'TEST_FAILED_BUT_REDUCED'
                elif defects4j_config["respond_test_output"] == defects4j_config["fixed_test_output"]:
                    defects4j_config["result_type"][str(sample_number)] = 'TEST_FAILED_BUT_MATCHED'
                else:
                    defects4j_config["result_type"][str(sample_number)] = 'TEST_FAILED'
            else:
                defects4j_config["result_type"][str(sample_number)] = 'APPLIED_BUT_COMPILED_FAILED'
        else:
            defects4j_config["result_type"][str(sample_number)] = 'ERROR'
            defects4j_config["error_message"] = str(error)
    return defects4j_config


def verify_single_sample(args, defects4j_config, sample_number):
    # record = get_result_by_id(id)

    benchmark = get_benchmark(args.benchmark)

    printlog('Verifying bug {} {}: sample {}-------\n'.format(args.project,
                                                              args.bug_id, sample_number))

    # Run buggy version to get the test output
    buggy_bug = checkout_buggy_version(
        benchmark, args.working_directory, args.project, args.bug_id)
    if buggy_bug is None:
        return

    # location of checkout bug dir
    bug_dir = os.path.join(args.working_directory, "%s_%s_%s" %
                           (args.benchmark, args.project, args.bug_id))
    buggy_bug_path = bug_dir + "_buggy/" + defects4j_config["buggy_file_path"]

    try:
        defects4j_config = verify_response(defects4j_config, buggy_bug_path, buggy_bug, sample_number)
    except Exception as e:
        defects4j_config["result_type"][str(sample_number)] = 'SAMPLE_ERROR'
        defects4j_config["error_message"] = str(
            'Error in processing response, in the sample: ' + str(sample_number) + ', ' + str(e))
    try:
        # revert the chatgpt response version to the original fixed version
        revert_response_to_buggy_version(
            bug_dir, benchmark, args.working_directory, args.project, args.bug_id)
    except Exception as e:
        defects4j_config["result_type"][str(sample_number)] = 'SAMPLE_ERROR'
        defects4j_config["error_message"] = str(
            'Error when reverting buggy code, in the sample: ' + str(sample_number) + ', ' + str(e))

    time.sleep(12)