def top_k(lst, k):
    k=len(lst) if k>len(lst) else k
    l=[]
    while len(l)!=k:
        m=lst[0]
        for i in lst:
            if i>m:
                m=i
        l.append(m)
        lst.remove(m)
    return l
