def top_k(lst, k):
    a=[]
    while lst:
        for i in lst:
            a.append(max(lst))
            lst.remove(max(lst))
    return a[0:k]
