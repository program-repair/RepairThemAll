def top_k(lst, k):

    newlst = []
    for i in range(k):
        newlst.append(max(lst))
        lst.remove(max(lst))
    return newlst
