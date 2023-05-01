def remove_extras(lst):
    answer = []
    for i in lst:
        unique = True
        for a in answer:
            if i == a:
                unique = False
                break
        if unique:
            answer += [i]
    return answer
