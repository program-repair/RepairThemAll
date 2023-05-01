def sort_age(lst):
    if len(lst) < 2:
        return lst
    new_lst = []
    while lst:
        max_age = lst[0][1]
        first = lst[0]
        for j in range(1, len(lst)):
            if lst[j][1] > max_age:
                max_age = lst[j][1]
                first = lst[j]
        new_lst.append(first)
        lst.remove(first)
    return new_lst
