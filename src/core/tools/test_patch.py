
from core.database.schema import Result
from core.tools.patch import is_line_contain_statement, load_patch_file


def test_is_line_contain_statement():
    assert is_line_contain_statement(
        "public static void main(String[] args) {") == True
    assert is_line_contain_statement("return x;") == True
    assert is_line_contain_statement("/* comment") == False
    assert is_line_contain_statement("* comment") == False
    assert is_line_contain_statement("*/") == False
    assert is_line_contain_statement("// comment") == False
    assert is_line_contain_statement("    {") == True
    assert is_line_contain_statement("    }") == True


def test_load_patch_file():
    mock_result = Result()
    patch_data, mock_result = load_patch_file(
        mock_result, 'src/fixtures/Defects4J_Closure_01.patch')
    assert len(patch_data) == 1
    assert patch_data[0].file_path == 'src/com/google/javascript/jscomp/RemoveUnusedVars.java'
    assert patch_data[0].sorted_changes() == [379, 380, 381]


def test_load_patch_file_with_multi_files():
    mock_result = Result()
    patch_data, mock_result = load_patch_file(
        mock_result, 'src/fixtures/Defects4J_Closure_30.patch')
    assert len(patch_data) == 2
    assert patch_data[0].file_path == 'src/com/google/javascript/jscomp/FlowSensitiveInlineVariables.java'
    assert patch_data[0].sorted_changes() == [157]
    assert patch_data[1].file_path == 'src/com/google/javascript/jscomp/MustBeReachingVariableDef.java'
    assert patch_data[1].sorted_changes() == [71, 397, 399,
                                              400, 401, 403, 435, 436, 437]
