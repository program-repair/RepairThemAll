
import whatthepatch
import pprint
import re


def is_line_countable(line):
    striped_line = line.strip()
    is_comment = re.match(r'^(//|/\*|\*|\*/)', striped_line)
    has_multi_chars = len(striped_line) > 1
    return not is_comment and has_multi_chars


def load_patch_file(file_path):
    countable_changes = []
    with open(file_path, 'r') as file:
        text = file.read()
    for diff in whatthepatch.parse_patch(text):
        pp = pprint.PrettyPrinter(indent=4)
        for change in diff.changes or []:
            if change.new == None and is_line_countable(change.line):
                countable_changes.append(change.old)
        pp.pprint(countable_changes)

    return countable_changes
