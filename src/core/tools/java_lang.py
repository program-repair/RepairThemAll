import javalang
import re

ACCEPTED_NODE_TYPES = ['MethodDeclaration', 'ConstructorDeclaration',
                       'ClassDeclaration', 'EnumDeclaration', 'InterfaceDeclaration']


class CodeLine:
    def __init__(self, number, content):
        self.number = number
        self.content = content

    def is_comment_line(self):
        return is_comment_line(self.content)

    def __str__(self):
        return f'{self.number}: {self.content}'


class JavaAstNode:
    def __init__(self, name='', type='', start_pos=0, end_pos=0):
        self.name = name
        self.type = type
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.code_snippet = []
        self.highlight_line_numbers = []

    def is_empty(self):
        return self.name == '' and self.start_pos == 0 and self.end_pos == 0

    def load_code_snippet(self, file_lines):
        self.end_pos = self.__cal_node_end_pos(file_lines)
        for num, line in enumerate(file_lines[self.start_pos - 1:self.end_pos]):
            self.code_snippet.append(CodeLine(self.start_pos + num, line))

    def add_highlight_line_number(self, line_number):
        self.highlight_line_numbers.append(line_number)

    def code_snippet_without_comments(self):
        return [line.content for line in self.code_snippet if not line.is_comment_line()]

    def code_snippet_with_comments(self):
        return [line.content for line in self.code_snippet]

    def code_size(self):
        return self.end_pos - self.start_pos + 1

    def __cal_node_end_pos(self, file_lines):
        current_pos = self.start_pos
        stack = []

        while current_pos < len(file_lines):
            line = file_lines[current_pos - 1]
            line = re.sub(r'".*"', '', line)
            line = re.sub(r"'.*'", '', line)
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

    def __str__(self):
        return "JavaAstNode(name={}, type={}, start_pos={}, end_pos={}, highlight=\n{})".format(self.name, self.type, self.start_pos, self.end_pos, self.highlight_line_numbers)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, JavaAstNode):
            return False
        return self.name == __o.name and self.type == __o.type and self.start_pos == __o.start_pos and self.end_pos == __o.end_pos and self.highlight_line_numbers == __o.highlight_line_numbers


def clean_code(lines):
    # remove right side trailing space
    lines = [line.rstrip() for line in lines]
    # remove empty lines
    lines = [x for x in lines if len(x) > 0]
    return '\n'.join(lines)


def is_comment_line(line):
    striped_line = line.strip()
    return bool(re.match(r'^(//|/\*|\*|\*/)', striped_line))


def is_line_contain_statement(line):
    striped_line = line.strip()
    is_comment = re.match(r'^(//|/\*|\*|\*/)', striped_line)
    has_multi_chars = len(striped_line) > 1
    return not is_comment and has_multi_chars


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


def load_ast_nodes(file_path):
    ast_nodes = []
    with open(file_path, 'r') as file:
        text = file.read()
        tree = javalang.parse.parse(text)
    with open(file_path, 'r') as file:
        file_lines = file.readlines()

    filtered_nodes = filter_ast_nodes_by_types(tree, ACCEPTED_NODE_TYPES)
    for filtered_node in filtered_nodes:
        ast_node = JavaAstNode(
            filtered_node.name, filtered_node.__class__.__name__, filtered_node.position.line)
        ast_node.load_code_snippet(file_lines)
        ast_nodes.append(ast_node)

    return ast_nodes


def load_patch_code_snippets(file_path, line_numbers):
    ast_nodes = load_ast_nodes(file_path)

    for line_number in line_numbers:
        for m in ast_nodes:
            if m.start_pos <= line_number and m.end_pos >= line_number:
                m.add_highlight_line_number(line_number)

    ast_nodes = list(filter(lambda n: len(
        n.highlight_line_numbers) > 0, ast_nodes))

    ast_nodes.sort(key=lambda n: n.code_size())

    most_related_method = JavaAstNode()
    for m in ast_nodes:
        if len(m.highlight_line_numbers) > 0:
            if most_related_method.is_empty() or len(m.highlight_line_numbers) > len(most_related_method.highlight_line_numbers):
                most_related_method = m

    return most_related_method
