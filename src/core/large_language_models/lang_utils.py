import javalang
import pprint
import re


class MethodNode:
    def __init__(self, name, start_pos, end_pos):
        self.name = name
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.code_snippet = []

    def __str__(self):
        return "MethodNode(name={}, start_pos={}, end_pos={})".format(self.name, self.start_pos, self.end_pos)


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


def is_line_countable(line):
    striped_line = line.strip()
    is_comment = re.match(r'^(//|/\*|\*|\*/)', striped_line)
    has_multi_chars = len(striped_line) > 1
    return not is_comment and has_multi_chars


def load_file_methods(file_path):
    pp = pprint.PrettyPrinter(indent=4)
    method_nodes = []

    with open(file_path, 'r') as file:
        text = file.read()
        tree = javalang.parse.parse(text)

    for _, node in tree.filter(javalang.parser.tree.MethodDeclaration):
        if node != None:
            method_nodes.append(MethodNode(
                node.name, node.position.line, 0))  # type: ignore

    return method_nodes


def parse_method_metainfo(file_path):
    pp = pprint.PrettyPrinter(indent=4)
    method_nodes = load_file_methods(file_path)
    file_lines = read_file_lines(file_path)

    for i in range(len(method_nodes)):
        if i == len(method_nodes) - 1:
            method_nodes[i].end_pos = len(file_lines)
        else:
            method_nodes[i].end_pos = method_nodes[i + 1].start_pos - 1

    return method_nodes
