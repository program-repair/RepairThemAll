def top_k(lst, k):
    res = []
    for i in range(k):
        res.append(max(lst))
        lst.remove(max(lst))
    return res
