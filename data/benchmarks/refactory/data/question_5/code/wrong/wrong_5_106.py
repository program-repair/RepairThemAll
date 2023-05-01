def top_k(lst, k):
    new = []
    lst.sort()
    for i in range(k-1):
        new.append(lst[i])
    return new
