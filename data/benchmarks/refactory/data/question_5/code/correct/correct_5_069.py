def top_k(lst, k):
    sort=[]
    for i in range (k):
        biggest=max(lst)
        lst.remove(biggest)
        sort.append(biggest)
    return sort
