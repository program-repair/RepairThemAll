
import whatthepatch
import re


class CountableDiff:
    def __init__(self, file_path=''):
        self.file_path = file_path
        self.changes = set()

    def sorted_changes(self):
        return sorted(self.changes)

    def __str__(self) -> str:
        return "CountableDiff(file_path={}, changes={})".format(self.file_path, self.sorted_changes())

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, CountableDiff):
            return False
        return self.file_path == __o.file_path and self.changes == __o.changes


def is_line_contain_statement(line):
    striped_line = line.strip()
    is_comment = re.match(r'^(//|/\*|\*|\*/)', striped_line)
    has_multi_chars = len(striped_line) > 0
    return not is_comment and has_multi_chars


def read_patch_file(file_path):
    countable_diffs = []
    with open(file_path, 'r') as file:
        text = file.read()

    for diff in whatthepatch.parse_patch(text):

        countable_diff = CountableDiff(getattr(diff.header, 'new_path'))
        for change in diff.changes or []:
            if change.new == None and is_line_contain_statement(change.line):
                countable_diff.changes.add(change.old)
        countable_diffs.append(countable_diff)

    return countable_diffs, text


def load_patch_file(result, file_path):
    countable_diffs = []
    with open(file_path, 'r') as file:
        text = file.read()

    if result:
        result.patch = text

    for diff in whatthepatch.parse_patch(text):

        countable_diff = CountableDiff(getattr(diff.header, 'new_path'))
        for change in diff.changes or []:
            if change.new == None and is_line_contain_statement(change.line):
                countable_diff.changes.add(change.old)
        countable_diffs.append(countable_diff)

    return countable_diffs, result
