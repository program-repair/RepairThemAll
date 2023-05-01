def top_k(lst, k):
    a=[]
    sort =[]
    while lst:
        biggest = lst[0]
        for i in lst:
            if (i)> biggest:
                biggest = i
        lst.remove(biggest)
        sort.append(biggest)
    for i in range(k):
        a = a + [sort[i],]
    return a
    pass
