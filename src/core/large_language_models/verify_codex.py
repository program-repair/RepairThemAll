import os
import shutil
import time
from dotenv import dotenv_values
import openai
from core.database.engine import get_result_by_id, update_result_by_id
from core.tools.log import printlog
from core.tools.persist import write_to_file
from core.utils import get_benchmark


config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')

CODE_TOO_LONG = "Code is too long"
CODEX_MODEL = "code-davinci-002"
EXAMPLE_BUGGY_FILEPATH = 'data/example/codex_prompt_example_buggy.source'
EXAMPLE_FIXED_FILEPATH = 'data/example/codex_prompt_example_fixed.source'
PROJECT_EXAMPLE_BUGGY_PATH_FORMAT = 'data/example/codex_project_example_{}_buggy.source'
PROJECT_EXAMPLE_FIXED_PATH_FORMAT = 'data/example/codex_project_example_{}_fixed.source'

STOP_SIGN = "###"


def apply_text_to_buggy_version(buggy_bug_path, record):
    printlog('fixed_bug_path: ', buggy_bug_path)
    printlog('response_text:\n ', record.respond_clean_code_chunk)
    try:
        response_text_lines = record.respond_clean_code_chunk.split("\n")
        with open(buggy_bug_path, 'r') as file:
            buggy_bug_lines = file.readlines()
        new_buggy_bug_file = "".join(buggy_bug_lines[0:record.bug_start_pos - 1]) + \
            "\n".join(response_text_lines) + \
            "".join(buggy_bug_lines[record.bug_end_pos:])
        write_to_file(buggy_bug_path, new_buggy_bug_file)
        return True, None
    except Exception as e:
        printlog('Error: ', e)
        printlog('buggy_bug_path: ', buggy_bug_path)
        return False, e


# revert fixed bug file after testing codex response
def revert_response_to_buggy_version(bug_dir, benchmark, working_directory, project, bug_id):
    printlog('revert buggy bug file after testing codex response')
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
        printlog('Something went wrong when checkout buggy version of bug {} {}-------\n'.format(project, bug_id), e)
        return None


def verify_response(record, buggy_bug_path, buggy_bug):
    if record.result_type == 'RESPONDED' or record.result_type == 'SAMPLE_ERROR':
        # apply the choice to the code
        applied, error = apply_text_to_buggy_version(buggy_bug_path, record)
        if applied:
            record.result_type = 'APPLIED'
            compiled_output = buggy_bug.compile()
            record.respond_compiled_output = compiled_output
            if compiled_output.count('OK') == 2:
                record.result_type = 'COMPILED_SUCCESS'
                # only run test if the code is compiled successfully
                success, test_output = buggy_bug.run_test()
                printlog('test_output: \n', test_output)
                record.respond_test_output = test_output
                if success == True:
                    record.result_type = 'TEST_SUCCESS'
                elif len(record.respond_test_output) < len(record.buggy_test_output) and record.respond_test_output == record.fixed_test_output:
                    record.result_type = 'TEST_FAILED_BUT_MATCHED_REDUCED'
                elif len(record.respond_test_output) < len(record.buggy_test_output):
                    record.result_type = 'TEST_FAILED_BUT_REDUCED'
                elif record.respond_test_output == record.fixed_test_output:
                    record.result_type = 'TEST_FAILED_BUT_MATCHED'
                else:
                    record.result_type = 'TEST_FAILED'
            else:
                record.result_type = 'APPLIED_BUT_COMPILED_FAILED'
        else:
            record.result_type = 'ERROR'
            record.error_message = str(error)
    return record


def verify_single_sample(id, working_directory):
    record = get_result_by_id(id)

    # Only support Codex with Defects4J for now
    if record.model != 'Codex' or record.benchmark != 'Defects4J':
        printlog('Only support Codex with Defects4J for now')
        exit(1)

    benchmark = get_benchmark(record.benchmark)

    printlog('Verifying bug {} {}: sample {}-------\n'.format(record.project,
          record.bug_id, record.sample_number))

    # Run buggy version to get the test output
    buggy_bug = checkout_buggy_version(
        benchmark, working_directory, record.project, record.bug_id)
    if buggy_bug is None:
        return

    # location of checkout bug dir
    bug_dir = os.path.join(working_directory, "%s_%s_%s" %
                           (record.benchmark, record.project, record.bug_id))
    buggy_bug_path = bug_dir + "_buggy/" + record.buggy_file_path

    try:
        record = verify_response(record, buggy_bug_path, buggy_bug)
    except Exception as e:
        record.result_type = 'SAMPLE_ERROR'
        record.error_message = str(
            'Error in processing response, in the sample: ' + str(record.sample_number) + ', ' + str(e))
    try:
        # revert the codex response version to the original fixed version
        revert_response_to_buggy_version(
            bug_dir, benchmark, working_directory, record.project, record.bug_id)
    except Exception as e:
        record.result_type = 'SAMPLE_ERROR'
        record.error_message = str(
            'Error when reverting buggy code, in the sample: ' + str(record.sample_number) + ', ' + str(e))
    update_result_by_id(record.id, record)

    time.sleep(12)
