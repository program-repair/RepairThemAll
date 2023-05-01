def remove_extras(lst):
    answer = []
    for x in lst:
        if x not in answer:
            answer.append(x)
    return answer
