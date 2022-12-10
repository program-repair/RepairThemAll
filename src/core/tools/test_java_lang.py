from core.tools.java_lang import *


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
    print(result)
    assert clean_code(
        lines) == "public static void main(String[] args) {\nreturn x;\n}"


def test_load_ast_node():
    file_path = "src/core/tools/test_java_lang.java"
    root = load_ast_nodes(file_path)
    print(root)
    assert len(root) == 1
    assert root[0].name == "main"
    assert root[0].start_pos == 1
    assert root[0].end_pos == 6
    assert root[0].highlight_line_numbers == [1, 2, 3, 4, 5, 6]
