def extract_code(choice_text):
    code = []
    cnt = 0
    for l in choice_text.split('\n'):
        if l.startswith('```'):
            if cnt == 0:
                cnt += 1
                continue
            else:
                break
        code.append(l)
    return '\n'.join(code)