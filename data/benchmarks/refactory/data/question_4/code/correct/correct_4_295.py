def sort_age(lst):
    if len(lst) == 1:
        return lst
    sort = []
    while lst:
        tup = lst[0]
        smallest = lst[0][1]
        for element in lst:
            if element[1] > smallest:
                smallest = element[1]
                tup = element
        lst.remove(tup)
        sort.append(tup)
    return sort
