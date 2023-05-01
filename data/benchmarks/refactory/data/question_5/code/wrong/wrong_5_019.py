def top_k(lst, k):
    arranged = []
    while k>0:
        lst.remove(max(lst))
        arranged.append(max(lst))
        k -= 1
    return arranged
    pass
