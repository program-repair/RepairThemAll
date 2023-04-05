import copy
import math
import os
import shutil
import time
import json
from dotenv import dotenv_values
import openai

# from core.database.engine import count_collected_samples_by_conditions, save
from core.database.schema import Result
from core.tools.java_lang import get_node_by_position, load_ast_nodes, load_origin_code_node
from core.tools.log import printlog
from core.tools.patch import load_patch_file, read_patch_file
from core.tools.persist import write_to_file
from core.tools.prompt import chatgpt_prompt_generation
from core.tools.tokenizer import calculate_request_counter, number_of_tokens
from core.utils import get_benchmark


config = dotenv_values(".env")
openai.api_key = config.get('OPENAI_API_KEY')
DEFS4J_HOME = config.get("DEFS4J_HOME")


def load_code_node(fixed_file_path, buggy_file_path, countable_diffs):
    fixed_node, i = load_origin_code_node(
        fixed_file_path, countable_diffs[0].sorted_changes())
    buggy_nodes = load_ast_nodes(buggy_file_path)
    buggy_node = get_node_by_position(buggy_nodes, fixed_node, i)
    return fixed_node, buggy_node


def request_chatgpt_pr(prompt, request_params):
    # https://beta.openai.com/docs/api-reference/completions/create
    response = openai.ChatCompletion.create(
        model=request_params['model'],
        messages=[{"role": "user", "content": prompt}],
        temperature=request_params['temperature'],
        top_p=request_params['top_p'],
        frequency_penalty=request_params['frequency_penalty'],
        presence_penalty=request_params['presence_penalty'],
    )
    printlog('--->', response)
    return response


def apply_text_to_buggy_version(buggy_bug_path, response_text, buggy_node):
    printlog('fixed_bug_path: ', buggy_bug_path)
    printlog('fixed_node: ', buggy_node)
    printlog('response_text:\n ', response_text)
    try:
        response_text_lines = response_text.split("\n")
        with open(buggy_bug_path, 'r') as file:
            buggy_bug_lines = file.readlines()
        new_buggy_bug_file = "".join(buggy_bug_lines[0:buggy_node.start_pos - 1]) + \
            "\n".join(response_text_lines) + \
            "".join(buggy_bug_lines[buggy_node.end_pos:])
        write_to_file(buggy_bug_path, new_buggy_bug_file)
        return True, None
    except Exception as e:
        printlog('Error: ', e)
        printlog('buggy_bug_path: ', buggy_bug_path)
        return False, e


def get_fixed_bug_path(bug_dir, patch_file_path):
    countable_diffs, _ = load_patch_file(None, patch_file_path)
    return bug_dir + "_fixed/" + countable_diffs[0].file_path


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
    bug_identifier = project + '_' + bug_id

    bug_path = os.path.join(working_directory,
                            "%s_%s_%s_%s" % (benchmark.name, project, bug_id, version))

    printlog('bug_identifier: ', bug_identifier)
    bug = benchmark.get_bug(bug_identifier)
    printlog('bug: ', bug)
    is_buggy_version = version == 'buggy'
    bug.checkout(bug_path, is_buggy_version)

    return bug


def checkout_buggy_version(defects4j_config, benchmark, working_directory, project, bug_id):
    try:
        # checkout buggy bug
        buggy_bug = checkout_bug(
            benchmark, working_directory, project, bug_id, 'buggy')

        complied_output = buggy_bug.compile()
        if complied_output.count('OK') == 2:
            _, buggy_test_output = buggy_bug.run_test()
            defects4j_config.buggy_test_output = buggy_test_output
            return defects4j_config, buggy_bug
        else:
            defects4j_config.buggy_test_output = 'Compile error'
            return defects4j_config, None
    except Exception as e:
        printlog(
            'Something went wrong when checkout buggy version of bug {} {}-------\n'.format(project, bug_id), e)
        return defects4j_config, None


def checkout_fixed_version(defects4j_config, benchmark, working_directory, project, bug_id):
    try:
        # checkout fixed bug
        fixed_bug = checkout_bug(
            benchmark, working_directory, project, bug_id, 'fixed')

        complied_output = fixed_bug.compile()
        if complied_output.count('OK') == 2:
            _, fixed_test_output = fixed_bug.run_test()
            defects4j_config.fixed_test_output = fixed_test_output
            return defects4j_config, fixed_bug
        else:
            defects4j_config.fixed_test_output = 'Compile error'
            return defects4j_config, None
    except Exception as e:
        printlog(
            'Something went wrong when checkout fixed version of bug {} {}-------\n'.format(project, bug_id), e)
        return defects4j_config, None


# def build_result_template(args, bug_id):
#     result_template = Result()
#     result_template.model = args.model
#     result_template.benchmark = args.benchmark
#     result_template.project = args.project
#     result_template.bug_id = bug_id
#     result_template.request_type = 'SINGLE_FUNCTION'
#     result_template.sample_number = 0
#     return result_template


def load_buggy_fixed_code_nodes(defects4j_config, working_directory, countable_diffs, fixed_bug, bug_id):
    # prepare fixed and buggy code ast node
    bug_dir = os.path.join(working_directory, "%s_%s_%s" %
                           (fixed_bug.benchmark, fixed_bug.project, bug_id))
    fixed_bug_path = bug_dir + "_fixed/" + countable_diffs[0].file_path
    buggy_bug_path = bug_dir + "_buggy/" + countable_diffs[0].file_path
    fixed_node, buggy_node = load_code_node(
        fixed_bug_path, buggy_bug_path, countable_diffs)

    defects4j_config.bug_start_pos = buggy_node.start_pos
    defects4j_config.bug_end_pos = buggy_node.end_pos
    
    # buggy_code_chunk and fixed_code_chunk with comments
    defects4j_config.buggy_code_chunk = buggy_node.code_lines_str()
    # defects4j_config.buggy_code_token = number_of_tokens(
    #     defects4j_config.buggy_code_chunk)
    defects4j_config.fixed_code_chunk = fixed_node.code_lines_str()
    # print("buggy_code_chunk: ", defects4j_config.buggy_code_chunk)
    # print("fixed_code_chunk: ", defects4j_config.fixed_code_chunk)

    # defects4j_config.fixed_code_token = number_of_tokens(
    #     defects4j_config.fixed_code_chunk)

    # run original fixed version unit tests
    # must checkout the fixed bug again
    # fixed_bug = checkout_bug(
    #     fixed_bug.benchmark, working_directory, fixed_bug.project, bug_id, 'fixed')
    # template_fixed_complied_output = fixed_bug.compile()
    # if template_fixed_complied_output.count('OK') == 2:
    #     _, fixed_test_output = fixed_bug.run_test()
    #     defects4j_config.fixed_test_output = fixed_test_output
    #     printlog('fixed_test_output: \n', fixed_test_output)
    # else:
    #     defects4j_config.fixed_test_output = 'Compile error'

    # run buggy code against fixed unit tests, then revert the source to the fixed code
    # applied, error, original_func_lines = apply_text_to_fixed_version(
    #     fixed_bug_path, buggy_node.code_lines_str(), fixed_node)
    # if applied:
    #     template_buggy_complied_output = fixed_bug.compile()
    #     if template_buggy_complied_output.count('OK') == 2:
    #         _, buggy_test_output = fixed_bug.run_test()
    #         defects4j_config.buggy_test_output = buggy_test_output
    #         printlog('buggy_test_output: \n', buggy_test_output)
    #     else:
    #         defects4j_config.buggy_test_output = 'Compile error'
    #     revert_response_to_fixed_version(
    #         original_func_lines, working_directory, fixed_bug, patch_file_path)

    return defects4j_config, fixed_node, buggy_node


def build_prompt(args, defects4j_config, fixed_bug, buggy_node, fixa_config, bug_dir):

    # output_file_path = 'output/{}'.format(bug_dir.split('/')[-1])
    prompt, prompt_size, bug_size = chatgpt_prompt_generation(args, buggy_node, fixa_config['include_document'], fixa_config['include_comments'])
    # write_to_file(output_file_path + '.codex_prompt', prompt) # output_file_path is the bug dir
    defects4j_config.prompt_text = prompt
    defects4j_config.prompt_size = prompt_size
    defects4j_config.buggy_code_token = bug_size

    return defects4j_config


def build_request_params(args, defects4j_config, fixa_config):
    temperature = args.temperature
    request_params = {
        'model': args.model,
        'temperature': temperature,
        'max_tokens': args.max_tokens,
        'top_p': args.top_p,
        'frequency_penalty': args.frequency_penalty,
        'presence_penalty': args.presence_penalty,
    }
    defects4j_config.request_params = request_params
    defects4j_config.prompt_params = fixa_config
    defects4j_config.temperature = request_params['temperature']

    return defects4j_config


def sanitize_choice_text(choice_text):
    cleaned_text = []
    for l in choice_text.split('\n'):
        if l.startswith('#'):
            continue
        if len(l.strip()) == 0:
            continue
        cleaned_text.append(l)
    return '\n'.join(cleaned_text)


def extract_code(choice_text):
    code = []
    for l in choice_text.split('\n'):
        if l.startswith('```'):
            continue
        if len(l.strip()) == 0:
            continue
        code.append(l)
    return '\n'.join(code)


def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


def ask_chatgpt(args, bug_id, defects4j_config, fixa_config):
    # Only support Codex with Defects4J for now
    if args.benchmark != 'Defects4J':
        printlog('Only support Defects4J now')
        exit(1)

    benchmark = get_benchmark(args.benchmark)

    # build a result template that will be used to save the result
    # result_template = build_result_template(args, bug_id)

    # Run fixed version to get the test output
    defects4j_config, fixed_bug = checkout_fixed_version(
        defects4j_config, benchmark, args.working_directory, args.project, bug_id)
    if fixed_bug is None:
        return

    # Run buggy version to get the test output
    defects4j_config, buggy_bug = checkout_buggy_version(
        defects4j_config, benchmark, args.working_directory, args.project, bug_id)
    if buggy_bug is None:
        return

    try:
        # read patch file
        patch_file_path = DEFS4J_HOME + '/projects/{}/patches/{}.src.patch'.format(
            args.project, bug_id)
        # print('patch_file_path: ', patch_file_path)
        countable_diffs, patch_text = read_patch_file(patch_file_path)
        # print("countable_diffs: ", countable_diffs[0])
        # print("countable_diffs: ", len(countable_diffs))
        # print("patch_text: ", patch_text)      
        defects4j_config.patch = patch_text
        if len(countable_diffs) > 1:
            defects4j_config.result_type = 'ERROR'
            defects4j_config.error_message = str(
                "Skip, more than one file changed")
            # save(defects4j_config)
            return

        defects4j_config.buggy_file_path = countable_diffs[0].file_path

        # location of checkout bug dir
        bug_dir = os.path.join(args.working_directory, "%s_%s_%s" %
                               (fixed_bug.benchmark, fixed_bug.project, bug_id))
        # prepare fixed and buggy code ast node
        # run original fixed version unit tests
        # run buggy code against fixed unit tests, then revert the source to the fixed code
        defects4j_config, fixed_node, buggy_node = load_buggy_fixed_code_nodes(
            defects4j_config, args.working_directory, countable_diffs, fixed_bug, bug_id)

        # build prompt
        # print("Start to build prompt...")
        defects4j_config = build_prompt(
            args, defects4j_config, fixed_bug, buggy_node, fixa_config, bug_dir)

        # calculate number of requests
        defects4j_config = build_request_params(
            args, defects4j_config, fixa_config)

        # send requests to Codex
        sample_number = 0
        curr_request_counter = 0
        openai_error_counter = 0
        target_path = args.working_directory + '/' + defects4j_config.benchmark + '/' + defects4j_config.project + '/' + str(defects4j_config.bug_id)
  
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        chatgpt_response = 'response{}.txt'
        max_openai_error_counter = int(
            config.get('MAX_OPENAI_ERROR_COUNTER') or 2)
        # save some related files
        write_to_file(os.path.join(target_path, 'prompt.txt'), defects4j_config.prompt_text)
        write_to_file(os.path.join(target_path, 'buggy_code.txt'), buggy_node.code_lines_str(fixa_config['include_comments']))
        write_to_file(os.path.join(target_path, 'fixed_code.txt'), fixed_node.code_lines_str(fixa_config['include_comments']))
        write_to_file(os.path.join(target_path, 'patch'), defects4j_config.patch)
        with open(os.path.join(target_path, 'defects4j_config.json'), 'w') as f:
            json.dump(defects4j_config, f, indent=4)

        if args.num_requests > 10:
            printlog('request_counter is too large, will reset to 10')
            args.num_requests = 10
        while curr_request_counter < args.num_requests and openai_error_counter < max_openai_error_counter:
            current_time = int(time.time())
            if defects4j_config.prompt_size > args.max_tokens:
                response = "Prompt size is too large, will skip"
                printlog(response)
                output_file_name = "response.txt"
                output_file_path = os.path.join(target_path, output_file_name)
                with open(output_file_path, 'w') as f:
                    f.write(response)
                break
            try:
                response = request_chatgpt_pr(
                    defects4j_config.prompt_text, defects4j_config.request_params)
                curr_request_counter += 1
                current_time = int(time.time())
                openai_error_counter = 0  # reset the error counter
            except Exception as e:
                if 'Rate limit reached for' in str(e):
                    # for defect4j, we may not face this error becasue we are far away from the limit
                    printlog('Rate limit reached for this bug, will skip', str(e))
                    time.sleep(60)
                elif 'Error communicating with OpenAI' in str(e):
                    # sometimes OpenAI will return error, we will retry
                    printlog('OpenAI server error, will retry', str(e))
                    time.sleep(60)
                else:
                    printlog('Something went wrong when performing requesting', str(e))
                    time.sleep(60)
                openai_error_counter += 1
                if openai_error_counter >= max_openai_error_counter:
                    raise e
                continue

            fixed_code = response['choices'][0]['message']['content']
            fixed_code = extract_code(fixed_code)
            output_file_path = os.path.join(target_path, chatgpt_response.format(str(curr_request_counter)))
            with open(output_file_path, 'w') as f:
                f.write(fixed_code)
    except Exception as e:
        defects4j_config.result_type = 'TEMPLATE_ERROR'
        defects4j_config.error_message = str(e)
        printlog('Error when processing bug: ', bug_id, str(e))
        time.sleep(12)
