
from core.tools.patch import is_line_contain_statement, load_patch_file


def test_is_line_contain_statement():
    assert is_line_contain_statement(
        "public static void main(String[] args) {") == True
    assert is_line_contain_statement("return x;") == True
    assert is_line_contain_statement("/* comment") == False
    assert is_line_contain_statement("* comment") == False
    assert is_line_contain_statement("*/") == False
    assert is_line_contain_statement("// comment") == False
    assert is_line_contain_statement("    {") == False
    assert is_line_contain_statement("    }") == False


def test_load_patch_file():
    result = load_patch_file('src/fixtures/Defects4J_Closure_01.patch')
    assert len(result) == 1
    assert result[0].file_path == 'src/com/google/javascript/jscomp/RemoveUnusedVars.java'
    assert result[0].sorted_changes() == [379, 380]


def test_load_patch_file_with_multi_files():
    result = load_patch_file('src/fixtures/Defects4J_Closure_30.patch')
    assert len(result) == 2
    assert result[0].file_path == 'src/com/google/javascript/jscomp/FlowSensitiveInlineVariables.java'
    assert result[0].sorted_changes() == [157]
    assert result[1].file_path == 'src/com/google/javascript/jscomp/MustBeReachingVariableDef.java'
    assert result[1].sorted_changes() == [71, 397, 399, 400, 401, 435, 436]
