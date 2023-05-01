def top_k(lst, k):
    arranged = []
    while k > 0:
        arranged.append(max(lst))
        lst.remove(max(lst))
        k = k-1
    return arranged
    pass
