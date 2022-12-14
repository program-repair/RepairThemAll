
from core.tools.patch import load_patch_file


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
