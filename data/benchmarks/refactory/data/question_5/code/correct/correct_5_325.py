def top_k(lst, k):
    res = []
    while len(res) != k:
        elem = max(lst)
        lst.remove(elem)
        res.append(elem)
    return res
