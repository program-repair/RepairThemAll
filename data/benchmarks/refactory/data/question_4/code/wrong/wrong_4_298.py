def sort_age(lst):
    a = []
    while lst:
        oldest = lst[0]
        for i in lst:
            if i[1] > oldest[1]:
                oldest = i
        lst.remove(oldest)
        a.append(oldest)
    pass
