def top_k(lst, k):
    s = []
    for i in range(k):
        t = 0
        for r in lst:
            if r >= t:
                t = r
        lst.remove(t)
        s.append(t)
    return s
