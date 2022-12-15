def generate_prompt(buggy_example_path, fixed_example_path, target_buggy_node):
    with open(buggy_example_path, 'r') as file:
        buggy_example_lines = file.readlines()
    buggy_example = "".join(buggy_example_lines)

    with open(fixed_example_path, 'r') as file:
        fixed_example_lines = file.readlines()
    fixed_example = "".join(fixed_example_lines)

    example_prompt = '#Provide a fix for the buggy function\n#Buggy Function\n{}#Fixed Function\n{}'.format(
        buggy_example, fixed_example)
    target_prompt = '#Provide a fix for the buggy function\n#Buggy Function\n{}#Fixed Function\n'.format(
        target_buggy_node.code_lines_str())

    return example_prompt + target_prompt
