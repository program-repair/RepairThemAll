def sort_age(lst):
    unsorted = lst
    sort = []
    while unsorted:
        oldest = unsorted[0]
        for i in unsorted[1:]:
            if i[1] > oldest[1]:
                oldest = i
        sort += [oldest,]
        unsorted.remove(oldest)
    return sort
