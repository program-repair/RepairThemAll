from core.large_language_models.codex import load_buggy_code_node
from core.tools.prompt import generate_prompt


def test_generate_prompt():
    example_buggy_filepath = 'data/example/codex_prompt_example_buggy.source'
    example_fixed_filepath = 'data/example/codex_prompt_example_fixed.source'
    project_buggy_filepath = 'data/example/codex_project_example_Closure_buggy.source'
    project_fixed_filepath = 'data/example/codex_project_example_Closure_fixed.source'
    target_buggy_filepath = 'src/fixtures/Defects4J_Closure_01_buggy.source'
    target_fixed_filepath = 'src/fixtures/Defects4J_Closure_01_fixed.source'
    target_patch_filepath = 'src/fixtures/Defects4J_Closure_01.patch'
    target_prompt_filepath = 'src/fixtures/Defects4J_Closure_01.prompt'

    fixed_node, buggy_node = load_buggy_code_node(
        target_fixed_filepath, target_buggy_filepath, target_patch_filepath)

    prompt = generate_prompt('###', example_buggy_filepath, example_fixed_filepath,
                             project_buggy_filepath, project_fixed_filepath, buggy_node, False, False, True)

    with open(target_prompt_filepath, 'r') as file:
        target_prompt_lines = file.readlines()
    expected = "".join(target_prompt_lines)
    assert prompt == expected
