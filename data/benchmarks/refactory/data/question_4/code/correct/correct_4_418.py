def sort_age(lst):
    new_lst = []
    while lst:
        oldest = lst[0]
        for a in lst:
            if a[1] > oldest[1]:
                oldest = a
        lst.remove(oldest)
        new_lst.append(oldest)
    return new_lst
