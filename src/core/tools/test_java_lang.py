import os
from core.tools.java_lang import *
from core.tools.patch import load_patch_file

FIXTURES_FIXED_NODES = {
    "Closure_01": JavaAstNode(name='removeUnreferencedFunctionArgs', type='MethodDeclaration', start_pos=369, end_pos=409, highlight_line_numbers=[379, 380]),
    "Closure_05": JavaAstNode(name='isInlinableObject', type='MethodDeclaration', start_pos=155, end_pos=256, highlight_line_numbers=[176, 177]),
    "Closure_10": JavaAstNode(name='mayBeString', type='MethodDeclaration', start_pos=1415, end_pos=1421, highlight_line_numbers=[1417]),
    "Closure_15": JavaAstNode(name='apply', type='MethodDeclaration', start_pos=84, end_pos=112, highlight_line_numbers=[102, 103]),
    "Closure_20": JavaAstNode(name='tryFoldSimpleFunctionCall', type='MethodDeclaration', start_pos=208, end_pos=231, highlight_line_numbers=[220, 221]),
    "Closure_25": JavaAstNode(name='traverseNew', type='MethodDeclaration', start_pos=1035, end_pos=1061, highlight_line_numbers=[1036, 1055]),
    "Closure_30_1": JavaAstNode(name='process', type='MethodDeclaration', start_pos=156, end_pos=158, highlight_line_numbers=[157]),
    "Closure_30_2": JavaAstNode(name='MustBeReachingVariableDef', type='ClassDeclaration', start_pos=45, end_pos=446, highlight_line_numbers=[71, 397, 399, 400, 401, 435, 436]),
    "Mockito_01": JavaAstNode(name='captureArgumentsFrom', type='MethodDeclaration', start_pos=120, end_pos=161, highlight_line_numbers=[123, 124, 125, 126, 129, 130, 131, 132]),
    "Mockito_05": JavaAstNode(name='verify', type='MethodDeclaration', start_pos=75, end_pos=99, highlight_line_numbers=[91]),
    "Mockito_10": JavaAstNode(name='ReturnsDeepStubs', type='ClassDeclaration', start_pos=43, end_pos=167, highlight_line_numbers=[72, 88, 89, 92, 96, 101, 105, 106]),
    "Mockito_15": JavaAstNode(name='thenInject', type='MethodDeclaration', start_pos=24, end_pos=33, highlight_line_numbers=[26]),
    "Mockito_20": JavaAstNode(name='createMock', type='MethodDeclaration', start_pos=24, end_pos=54, highlight_line_numbers=[32, 35, 46]),
    "Mockito_25": JavaAstNode(name='ReturnsDeepStubs', type='ClassDeclaration', start_pos=41, end_pos=121, highlight_line_numbers=[56, 59, 71, 80, 81, 82, 83, 84, 87, 88, 89, 90, 91, 93, 94, 97, 98, 99, 100, 101, 103, 106]),
    "Mockito_30_1": JavaAstNode(name='smartNullPointerException', type='MethodDeclaration', start_pos=438, end_pos=447, highlight_line_numbers=[438, 442]),
    "Mockito_30_2": JavaAstNode(name='intercept', type='MethodDeclaration', start_pos=51, end_pos=58, highlight_line_numbers=[56])
}


def test_is_comment_line():
    assert is_comment_line("public static void main(String[] args) {") == False
    assert is_comment_line("return x;") == False
    assert is_comment_line("/* comment") == True
    assert is_comment_line("* comment") == True
    assert is_comment_line("*/") == True
    assert is_comment_line("// comment") == True


def test_clean_code():
    lines = ["public static void main(String[] args) {    ", "return x;    ",
             "", "}    "]
    result = clean_code(lines)
    assert clean_code(
        lines) == "public static void main(String[] args) {\nreturn x;\n}"


def test_load_ast_node():
    file_path = "src/fixtures/Defects4J_Closure_01_fixed.source"
    expect_nodes = [
        JavaAstNode(name='RemoveUnusedVars',
                    type='ClassDeclaration', start_pos=69, end_pos=998),
        JavaAstNode(name='RemoveUnusedVars',
                    type='ConstructorDeclaration', start_pos=123, end_pos=133),
        JavaAstNode(name='process', type='MethodDeclaration',
                    start_pos=140, end_pos=150),
        JavaAstNode(name='process', type='MethodDeclaration',
                    start_pos=153, end_pos=163),
        JavaAstNode(name='traverseAndRemoveUnusedReferences',
                    type='MethodDeclaration', start_pos=168, end_pos=181),
        JavaAstNode(name='traverseNode', type='MethodDeclaration',
                    start_pos=192, end_pos=305),
        JavaAstNode(name='isRemovableVar', type='MethodDeclaration',
                    start_pos=307, end_pos=324),
        JavaAstNode(name='traverseFunction',
                    type='MethodDeclaration', start_pos=334, end_pos=348),
        JavaAstNode(name='collectMaybeUnreferencedVars',
                    type='MethodDeclaration', start_pos=354, end_pos=361),
        JavaAstNode(name='removeUnreferencedFunctionArgs',
                    type='MethodDeclaration', start_pos=369, end_pos=409),
        JavaAstNode(name='getFunctionArgList',
                    type='MethodDeclaration', start_pos=415, end_pos=417),
        JavaAstNode(name='CallSiteOptimizer',
                    type='ClassDeclaration', start_pos=419, end_pos=702),
        JavaAstNode(name='CallSiteOptimizer',
                    type='ConstructorDeclaration', start_pos=425, end_pos=430),
        JavaAstNode(name='optimize', type='MethodDeclaration',
                    start_pos=432, end_pos=443),
        JavaAstNode(name='applyChanges', type='MethodDeclaration',
                    start_pos=448, end_pos=457),
        JavaAstNode(name='markUnreferencedFunctionArgs',
                    type='MethodDeclaration', start_pos=472, end_pos=510),
        JavaAstNode(name='canRemoveArgFromCallSites',
                    type='MethodDeclaration', start_pos=517, end_pos=535),
        JavaAstNode(name='tryRemoveArgFromCallSites',
                    type='MethodDeclaration', start_pos=541, end_pos=566),
        JavaAstNode(name='tryRemoveAllFollowingArgs',
                    type='MethodDeclaration', start_pos=571, end_pos=585),
        JavaAstNode(name='getArgumentForCallOrNewOrDotCall',
                    type='MethodDeclaration', start_pos=591, end_pos=599),
        JavaAstNode(name='canModifyCallers',
                    type='MethodDeclaration', start_pos=605, end_pos=624),
        JavaAstNode(name='isModifiableCallSite',
                    type='MethodDeclaration', start_pos=630, end_pos=633),
        JavaAstNode(name='canChangeSignature',
                    type='MethodDeclaration', start_pos=639, end_pos=687),
        JavaAstNode(name='getFunctionDefinition',
                    type='MethodDeclaration', start_pos=693, end_pos=701),
        JavaAstNode(name='interpretAssigns',
                    type='MethodDeclaration', start_pos=724, end_pos=773),
        JavaAstNode(name='removeAllAssigns',
                    type='MethodDeclaration', start_pos=778, end_pos=783),
        JavaAstNode(name='markReferencedVar',
                    type='MethodDeclaration', start_pos=790, end_pos=798),
        JavaAstNode(name='removeUnreferencedVars',
                    type='MethodDeclaration', start_pos=804, end_pos=870),
        JavaAstNode(name='Continuation', type='ClassDeclaration',
                    start_pos=877, end_pos=896),
        JavaAstNode(name='Continuation',
                    type='ConstructorDeclaration', start_pos=881, end_pos=884),
        JavaAstNode(name='apply', type='MethodDeclaration',
                    start_pos=886, end_pos=895),
        JavaAstNode(name='Assign', type='ClassDeclaration',
                    start_pos=898, end_pos=997),
        JavaAstNode(name='Assign', type='ConstructorDeclaration',
                    start_pos=922, end_pos=933),
        JavaAstNode(name='maybeCreateAssign',
                    type='MethodDeclaration', start_pos=939, end_pos=965),
        JavaAstNode(name='remove', type='MethodDeclaration',
                    start_pos=970, end_pos=996),
    ]
    result_nodes = load_ast_nodes(file_path)
    assert len(result_nodes) == 35
    for i in range(len(result_nodes)):
        assert result_nodes[i].__eq__(expect_nodes[i])


def test_load_fixed_code_node():
    countable_diffs = load_patch_file(
        "src/fixtures/Defects4J_Closure_01.patch")
    file_path = "src/fixtures/Defects4J_Closure_01_fixed.source"
    result = load_fixed_code_node(
        file_path, countable_diffs[0].sorted_changes())
    expect = JavaAstNode(name='removeUnreferencedFunctionArgs',
                         type='MethodDeclaration', start_pos=369, end_pos=409)
    expect.highlight_line_numbers = [379, 380]
    assert result.__eq__(expect)


def test_load_fixed_code_node_all_fixtures():
    print('test_load_fixed_code_node_all_fixtures:')
    fixture_path = "src/fixtures/"
    projects = ["Closure", "Mockito"]
    examples = ["01", "05", "10", "15", "20", "25", "30"]
    for project in projects:
        for example in examples:
            # read patch diffs
            patch_file_path = os.path.join(
                fixture_path, "Defects4J_{}_{}.patch".format(project, example))
            countable_diffs = load_patch_file(patch_file_path)
            # fixed ast node
            if len(countable_diffs) == 1:
                fixed_file_path = os.path.join(
                    fixture_path, "Defects4J_{}_{}_fixed.source".format(project, example))
                result = load_fixed_code_node(
                    fixed_file_path, countable_diffs[0].sorted_changes())
                print('fixed node for {}_{}: {}'.format(
                    project, example, result))
                expect = FIXTURES_FIXED_NODES["{}_{}".format(project, example)]
                assert result.__eq__(expect)
            elif len(countable_diffs) > 1:
                for i in range(len(countable_diffs)):
                    fixed_file_path = os.path.join(
                        fixture_path, "Defects4J_{}_{}_{}_fixed.source".format(project, example, i + 1))
                    result = load_fixed_code_node(
                        fixed_file_path, countable_diffs[i].sorted_changes())
                    print('fixed node for {}_{}_{}: {}'.format(
                        project, example, i + 1, result))
                    expect = FIXTURES_FIXED_NODES["{}_{}_{}".format(
                        project, example, i + 1, result)]
                    assert result.__eq__(expect)


def test_get_node_by_hash():
    fixed_file_path = "src/fixtures/Defects4J_Closure_01_fixed.source"
    buggy_file_path = "src/fixtures/Defects4J_Closure_01_buggy.source"
    patch_file_path = 'src/fixtures/Defects4J_Closure_01.patch'
    countable_diffs = load_patch_file(patch_file_path)
    fixed_node = load_fixed_code_node(
        fixed_file_path, countable_diffs[0].sorted_changes())
    buggy_nodes = load_ast_nodes(buggy_file_path)
    buggy_node = get_node_by_hash(buggy_nodes, fixed_node.hash)
    print('fixed_node: ', fixed_node)
    print('buggy_node: ', buggy_node)
    assert buggy_node.hash == fixed_node.hash
