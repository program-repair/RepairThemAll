def sort_age(lst):
    sort = []
    while lst:
        oldest = lst[0]
        for i in lst:
            if i[1]>oldest[1]:
                oldest = i
        lst.remove(oldest)
        sort.append(oldest)
    return sort
            
