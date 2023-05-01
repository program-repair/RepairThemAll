def sort_age(lst):
    store = []
    oldest = lst[0]
    for i in lst[1:]:
        if i[1] > oldest[1]:
            oldest = i
        lst.remove(oldest)
        sort.append(oldest)
    return sort
