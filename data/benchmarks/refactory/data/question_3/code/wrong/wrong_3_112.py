def remove_extras(lst):
    answer = []
    for i in lst:
        for a in answer:
            if i == a:
                break
        answer += i
    return answer
