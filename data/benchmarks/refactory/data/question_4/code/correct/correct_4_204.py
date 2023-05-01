def sort_age(lst):
    result = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        result.append(largest)
    return result
    pass
