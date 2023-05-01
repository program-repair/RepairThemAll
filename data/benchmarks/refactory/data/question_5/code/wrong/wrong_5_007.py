def top_k(lst, k):
    lst1 = []
    for i in lst:
        if i >= k:
            lst1.append(i) 
    sort = []
    while lst1: 
        biggest = lst[0]
        for element in lst1:
            if element > biggest:
                biggest = element
        lst1.remove(biggest)
        sort.append(biggest)
    return sort
