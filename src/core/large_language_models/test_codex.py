
from core.large_language_models.codex import load_buggy_code_node


def test_load_buggy_code_node():
    fixed_file_path = "src/fixtures/Defects4J_Closure_01_fixed.source"
    buggy_file_path = "src/fixtures/Defects4J_Closure_01_buggy.source"
    patch_file_path = 'src/fixtures/Defects4J_Closure_01.patch'
    fixed_node, buggy_node = load_buggy_code_node(
        fixed_file_path, buggy_file_path, patch_file_path)
    assert buggy_node.name == 'removeUnreferencedFunctionArgs'
    assert buggy_node.type == 'MethodDeclaration'
    assert buggy_node.start_pos == 369
    assert buggy_node.end_pos == 406
    print('buggy code body:\n', buggy_node.code_lines_str())
