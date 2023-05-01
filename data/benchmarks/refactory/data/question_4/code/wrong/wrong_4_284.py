def sort_age(lst):
    newlist = []
    while lst:
        oldest = lst[0]
        for i in lst:
            if i[1] > oldest:
                oldest = i
            else:
                continue
        lst.remove(oldest)
        newlist.append(oldest)
    return newlist
