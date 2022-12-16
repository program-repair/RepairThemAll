import javalang
from core.tools.java_ast_node import JavaAstNode

ACCEPTED_NODE_TYPES = ['MethodDeclaration', 'ConstructorDeclaration',
                       'ClassDeclaration', 'EnumDeclaration', 'InterfaceDeclaration']


def clean_code(lines):
    # remove right side trailing space
    lines = [line.rstrip() for line in lines]
    # remove empty lines
    lines = [x for x in lines if len(x) > 0]
    return '\n'.join(lines)


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


class NodeNotFoundException(Exception):
    pass


def get_node_by_hash(ast_nodes, hash):
    for node in ast_nodes:
        if node.hash == hash:
            return node
    raise NodeNotFoundException('Node with hash {} not found'.format(hash))
