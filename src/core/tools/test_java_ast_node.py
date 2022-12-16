
from core.tools.java_ast_node import is_comment_line


def test_is_comment_line():
    assert is_comment_line("public static void main(String[] args) {") == False
    assert is_comment_line("return x;") == False
    assert is_comment_line("/* comment") == True
    assert is_comment_line("* comment") == True
    assert is_comment_line("*/") == True
    assert is_comment_line("// comment") == True


def test_ast_node_hash():
    # TODO: implement this test
    pass
