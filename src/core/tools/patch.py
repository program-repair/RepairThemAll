
import whatthepatch
from core.tools.java_lang import is_line_contain_statement


def load_patch_file(file_path):
    countable_changes = []
    with open(file_path, 'r') as file:
        text = file.read()
    for diff in whatthepatch.parse_patch(text):
        for change in diff.changes or []:
            if change.new == None and is_line_contain_statement(change.line):
                countable_changes.append(change.old)
        print(countable_changes)

    return countable_changes
