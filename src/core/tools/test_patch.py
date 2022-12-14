
from core.tools.patch import load_patch_file


def test_load_patch_file():
    result = load_patch_file('src/fixtures/Defects4J_Closure_01.patch')
    assert result == [379, 380]
