def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]
        for i in lst:
            if largest[1] < i[1]:
                largest = i
            else:
                continue
        lst.remove(largest)
        sort.append(largest)
    return sort
