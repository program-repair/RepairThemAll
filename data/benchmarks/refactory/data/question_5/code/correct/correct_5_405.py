def top_k(lst,k): #k is the number of values in the lst
    lst2 = []
    while lst:
        a = max(lst)
        lst2.append(a)
        lst.remove(a)
    return lst2[0:k]
