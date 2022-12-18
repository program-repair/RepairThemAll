def generate_prompt(stop_sign, buggy_example_path, fixed_example_path, target_buggy_node, include_document, include_comments):
    with open(buggy_example_path, 'r') as file:
        buggy_example_lines = file.readlines()
    buggy_example = "".join(buggy_example_lines)

    with open(fixed_example_path, 'r') as file:
        fixed_example_lines = file.readlines()
    fixed_example = "".join(fixed_example_lines)

    example_prompt = '{}Provide a fix for the buggy function\n{}Buggy Function\n{}{}Fixed Function\n{}'.format(stop_sign, stop_sign,
                                                                                                               buggy_example, stop_sign, fixed_example)

    buggy_code = ''
    if include_document:
        buggy_code += target_buggy_node.documentation
        buggy_code += '\n'
    buggy_code += target_buggy_node.code_lines_str(include_comments)

    target_prompt = '{}Provide a fix for the buggy function\n{}Buggy Function\n{}{}Fixed Function\n'.format(
        stop_sign, stop_sign, buggy_code, stop_sign)

    return example_prompt + target_prompt
