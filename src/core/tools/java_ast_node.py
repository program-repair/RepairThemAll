import hashlib
import re


def is_comment_line(line):
    striped_line = line.strip()
    return bool(re.match(r'^(//|/\*|\*|\*/)', striped_line))


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
        self.documentation = ''

    def load_node_data(self, ast_node):
        self.documentation = ast_node.documentation

        hash_str = ''
        hash_str += ast_node.name
        hash_str += ast_node.__class__.__name__
        hash_str += str(ast_node.modifiers)
        hash_str += str(ast_node.annotations)

        if self.type in ['MethodDeclaration', 'ConstructorDeclaration']:
            hash_str += str(ast_node.type_parameters)
            hash_str += str(ast_node.parameters)
            hash_str += str(ast_node.throws)
        elif self.type in ['ClassDeclaration', 'InterfaceDeclaration']:
            hash_str += str(ast_node.type_parameters)

        self.hash = hashlib.sha256(hash_str.encode('utf-8')).hexdigest()

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
        return "JavaAstNode(name={}, type={}, start_pos={}, end_pos={}, hash={}, highlight_line_numbers=\n{})".format(self.name, self.type, self.start_pos, self.end_pos, self.hash, self.highlight_line_numbers)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, JavaAstNode):
            return False
        return self.name == __o.name and self.type == __o.type and self.start_pos == __o.start_pos and self.end_pos == __o.end_pos and self.highlight_line_numbers == __o.highlight_line_numbers
