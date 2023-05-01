def top_k(lst,k):
    nlst = []
    for x in range(k):
        b = max(lst)
        nlst.append(b)
        lst.remove(b)
    return nlst
