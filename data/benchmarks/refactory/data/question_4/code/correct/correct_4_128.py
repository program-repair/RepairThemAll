def sort_age(lst):
    answer = []
    while lst:
        largest = lst[0]
        for entry in lst:
            if entry[1] > largest[1]:
                largest = entry
        answer.append(largest)
        lst.remove(largest)
    return answer
