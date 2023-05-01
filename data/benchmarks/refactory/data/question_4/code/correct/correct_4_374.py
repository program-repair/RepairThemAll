def sort_age(lst):
    result = []
    while lst:
        largest = lst[0][1]
        index = 0
        for i in range(len(lst)):
            if lst[i][1] > largest:
                index = i
                largest = lst[i][1]
        result.append(lst[index])
        lst.remove(lst[index])
    return result
