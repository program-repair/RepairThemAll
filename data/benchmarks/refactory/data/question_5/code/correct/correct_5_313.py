def top_k(lst, k):
    new, a = [], lst[0]
    while lst:
        for i in range(len(lst)):
            new.append(max(lst))
            lst.remove(max(lst))
    return new[:k]
    pass
