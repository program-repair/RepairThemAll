def top_k(lst, k):
    newlst = []
    while len(newlst)<k:
        maximum = lst[0]
        for i in lst:
            if i > maximum:
                maximum = i
        newlst.append(maximum)
        lst.remove(maximum)
    return newlst
            
