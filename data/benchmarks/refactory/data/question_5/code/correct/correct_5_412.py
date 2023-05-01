def top_k(lst, k):
    sort = []
    sort_top_k = []
    while lst:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    
    if len(sort) < k:
        k = len(sort)
    for i in range(k):
        sort_top_k.append(sort[i])
    
    return sort_top_k
