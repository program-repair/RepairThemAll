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
    def __init__(self, name='', type='', start_pos=0, end_pos=0, highlight_line_numbers=[]):
        self.name = name
        self.type = type
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.code_snippet = []
        if highlight_line_numbers:
            self.highlight_line_numbers = highlight_line_numbers
        else:
            self.highlight_line_numbers = []
        self.hash = ''

    def generate_hash(self, ast_node):
        if type in ['MethodDeclaration', 'ConstructorDeclaration', 'ClassDeclaration', 'InterfaceDeclaration']:
            self.hash = hash((ast_node.name, ast_node.__class__.__name__,
                             str(ast_node.modifiers), str(ast_node.annotations), str(ast_node.type_parameters)))
        else:
            self.hash = hash((ast_node.name, ast_node.__class__.__name__,
                              str(ast_node.modifiers), str(ast_node.annotations)))

    def is_empty(self):
        return self.name == '' and self.start_pos == 0 and self.end_pos == 0

    def load_code_snippet(self, file_lines):
        self.end_pos = self.__cal_node_end_pos(file_lines)
        for num, line in enumerate(file_lines[self.start_pos - 1:self.end_pos]):
            self.code_snippet.append(CodeLine(self.start_pos + num, line))

    def add_highlight_line_number(self, line_number):
        self.highlight_line_numbers.append(line_number)

    def code_lines(self, include_comment_line=True):
        if include_comment_line:
            return [line.content for line in self.code_snippet]
        else:
            return [line.content for line in self.code_snippet if not line.is_comment_line()]

    def code_lines_str(self, include_comment_line=True):
        return "".join(self.code_lines(include_comment_line))

    def code_size(self):
        return self.end_pos - self.start_pos + 1

    def __cal_node_end_pos(self, file_lines):
        try:
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
                    elif c == ';':
                        if len(stack) == 0:
                            return current_pos
                current_pos += 1

            return current_pos
        except Exception as e:
            print('Error in __cal_node_end_pos: {} {} {}\n{}'.format(
                self.name, self.type, self.start_pos, e))
            raise e

    def __str__(self):
        return "JavaAstNode(name={}, type={}, start_pos={}, end_pos={}, hash={}, highlight=\n{})".format(self.name, self.type, self.start_pos, self.end_pos, self.hash, self.highlight_line_numbers)

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
        ast_node.generate_hash(filtered_node)
        ast_nodes.append(ast_node)

    return ast_nodes


def load_fixed_code_node(file_path, line_numbers):
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


def get_node_by_hash(ast_nodes, hash):
    for node in ast_nodes:
        if node.hash == hash:
            return node
    return JavaAstNode()
