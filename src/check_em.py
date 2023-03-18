
from core.database.engine import find_all_success
from core.tools.java_lang import find_exact_match
from core.tools.patch import is_line_contain_statement


def sanitize_code_chunk(code_chunk):
    lines = []
    for line in code_chunk.split('\n'):
        # is_line_contain_statement
        if len(line.strip()) == 0:
            continue
        if is_line_contain_statement(line):
            lines.append(line)
    return lines


if __name__ == "__main__":
    exact_match_counter = 0
    em_bugs = []
    success_samples = find_all_success()
    print('Total success samples: {}'.format(len(success_samples)))
    for sample in success_samples:
        if find_exact_match(sample):
            exact_match_counter += 1
            em_bugs.append('{}-{}'.format(sample.project, sample.bug_id))

    print('Total exact match: {}'.format(exact_match_counter))
    uniq_bugs = sorted(set(em_bugs))
    print('Total unique bugs: {}'.format(len(uniq_bugs)))
    for ub in uniq_bugs:
        print(ub)
