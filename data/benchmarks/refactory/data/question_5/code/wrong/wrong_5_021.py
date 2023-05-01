def top_k(lst, k):
    r=[]
    for qwerty in range(0,k):
        biggest=lst[0]
        for k in lst:
            if biggest<k:
                biggest=k
        r.append[biggest]
        lst.remove[biggest]
    return r
        
