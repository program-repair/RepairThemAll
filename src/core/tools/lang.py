import javalang
import re


class JavaAstNode:
    def __init__(self, name='', start_pos=0, end_pos=0):
        self.name = name
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.code_snippet = []
        self.highlight_line_numbers = []

    def is_empty(self):
        return self.name == '' and self.start_pos == 0 and self.end_pos == 0

    def __str__(self):
        return "JavaAstNode(name={}, start_pos={}, end_pos={}, highlight=\n{})".format(self.name, self.start_pos, self.end_pos, self.highlight_line_numbers)

    def add_highlight_line_number(self, line_number):
        self.highlight_line_numbers.append(line_number)


def clean_code(lines):
    # remove right side trailing space
    lines = [line.rstrip() for line in lines]
    # remove empty lines
    lines = [x for x in lines if x]
    return '\n'.join(lines)


def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def is_comment_line(line):
    striped_line = line.strip()
    return re.match(r'^(//|/\*|\*|\*/)', striped_line)


def filter_ast_nodes_by_types(root, node_types):
    filtered_nodes = []
    for node in root:
        if isinstance(node, tuple):
            for t in node:
                if not isinstance(t, tuple):
                    if t.__class__.__name__ in node_types:
                        filtered_nodes.append(t)
        else:
            if node.__class__.__name__ in node_types:
                filtered_nodes.append(node)

    return filtered_nodes


def filter_ast_nodes(file_path):
    method_nodes = []
    with open(file_path, 'r') as file:
        text = file.read()
        tree = javalang.parse.parse(text)

    filtered_nodes = filter_ast_nodes_by_types(
        tree, ['MethodDeclaration', 'ConstructorDeclaration', 'ClassDeclaration', 'EnumDeclaration', 'InterfaceDeclaration'])
    for filtered_node in filtered_nodes:
        method_nodes.append(JavaAstNode(filtered_node.name,
                            filtered_node.position.line))

    return method_nodes


def remove_string_from_line(line):
    line = re.sub(r'".*"', '', line)
    line = re.sub(r"'.*'", '', line)
    return line


def cal_method_end_pos(method_node, file_lines):
    current_pos = method_node.start_pos
    stack = []

    while current_pos < len(file_lines):
        line = file_lines[current_pos - 1]
        line = remove_string_from_line(line)
        if is_comment_line(line):
            current_pos += 1
            continue
        for c in line:
            if c == '{':
                stack.append(c)
            elif c == '}':
                stack.pop()
                if len(stack) == 0:
                    return current_pos
        current_pos += 1

    return current_pos


def parse_method_metainfo(file_path):
    method_nodes = filter_ast_nodes(file_path)
    file_lines = read_file_lines(file_path)

    for i in range(len(method_nodes)):
        method_nodes[i].end_pos = cal_method_end_pos(
            method_nodes[i], file_lines)

    return method_nodes


def load_patch_code_snippets(file_path, line_numbers):
    method_nodes = parse_method_metainfo(file_path)
    file_lines = read_file_lines(file_path)

    for m in method_nodes:
        m.code_snippet = file_lines[m.start_pos - 1:m.end_pos]

    for line_number in line_numbers:
        for m in method_nodes:
            if m.start_pos <= line_number and m.end_pos >= line_number:
                m.add_highlight_line_number(line_number)

    for m in method_nodes:
        print(m)

    most_related_method = JavaAstNode()
    for m in method_nodes:
        if len(m.highlight_line_numbers) > 0:
            if most_related_method.is_empty() or len(m.highlight_line_numbers) > len(most_related_method.highlight_line_numbers):
                most_related_method = m

    return most_related_method
