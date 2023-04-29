from core.tools.tokenizer import number_of_tokens, chatgpt_tokenize


def generate_prompt(stop_sign, first_buggy_example_path, first_fixed_example_path, project_buggy_path, project_fixed_path, target_buggy_node, include_document, include_comments, include_project_specific_example):
    # load general example
    with open(first_buggy_example_path, 'r') as file:
        first_buggy_example_lines = file.readlines()
    first_buggy_example = "".join(first_buggy_example_lines)
    with open(first_fixed_example_path, 'r') as file:
        first_fixed_example_lines = file.readlines()
    first_fixed_example = "".join(first_fixed_example_lines)
    general_example_prompt = '{}Provide a fix for the buggy function\n{}Buggy Function\n{}\n{}Fixed Function\n{}\n'.format(stop_sign, stop_sign,
                                                                                                                           first_buggy_example, stop_sign, first_fixed_example)

    # load project example
    project_example_prompt = ''
    if include_project_specific_example:
        with open(project_buggy_path, 'r') as file:
            project_buggy_example_lines = file.readlines()
        project_buggy_example = "".join(project_buggy_example_lines)
        with open(project_fixed_path, 'r') as file:
            project_fixed_example_lines = file.readlines()
        project_fixed_example = "".join(project_fixed_example_lines)
        project_example_prompt = '{}Provide a fix for the buggy function\n{}Buggy Function\n{}\n{}Fixed Function\n{}\n'.format(stop_sign, stop_sign,
                                                                                                                               project_buggy_example, stop_sign, project_fixed_example)

    # load target buggy function
    buggy_code = ''
    if include_document:
        buggy_code += target_buggy_node.documentation
        buggy_code += '\n'
    buggy_code += target_buggy_node.code_lines_str(include_comments)

    # combine all
    target_prompt = '{}Provide a fix for the buggy function\n{}Buggy Function\n{}\n{}Fixed Function\n'.format(
        stop_sign, stop_sign, buggy_code, stop_sign)

    # size
    prompt_size = number_of_tokens(
        general_example_prompt + project_example_prompt)
    bug_size = number_of_tokens(target_prompt)

    return (general_example_prompt + project_example_prompt + target_prompt), prompt_size, bug_size


def chatgpt_prompt_generation(args, target_buggy_node, include_document, include_comments):
    # load target buggy function
    buggy_code = ''
    if include_document:
        buggy_code += target_buggy_node.documentation
        buggy_code += '\n'
    buggy_code += target_buggy_node.code_lines_str(include_comments)

    bug_size = chatgpt_tokenize(buggy_code, args.model)

    buggy_lines = buggy_code.split('\n')
    prefix = '```'
    postfix = '```'
    buggy_format_code = prefix + '\n' + '\n'.join(buggy_lines) + '\n' + postfix

    if args.prompt_level == 'easy':
        target_prompt = args.prompt + buggy_code
        prompt_size = chatgpt_tokenize(target_prompt, args.model)

    elif args.prompt_level == 'advanced':
        target_prompt = [args.prompt, buggy_format_code]
        prompt_size = 0
        for each in target_prompt:
            prompt_size += chatgpt_tokenize(each, args.model)


    return target_prompt, prompt_size, bug_size