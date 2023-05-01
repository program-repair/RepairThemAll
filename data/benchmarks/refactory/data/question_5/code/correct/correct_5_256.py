def top_k(lst, k):
    count=0
    newlst=[]
    while lst:
        newlst+=[max(lst)]
        lst.remove(max(lst))
    for i in range(k):
        lst.append(newlst[i])
    return lst
