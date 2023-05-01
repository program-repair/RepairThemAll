def top_k(lst, k):
    if k == 0:
        return []
    if lst == []:
        return lst
    sort = []
    while lst:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
        if len(sort) == k:
            return sort
        else:
            continue
