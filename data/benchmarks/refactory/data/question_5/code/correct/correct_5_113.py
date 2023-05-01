def top_k(lst, k):
    n = len(lst)
    new =[]
    for i in range(0,n):
        largest = max(lst)
        lst.remove(largest)
        new.append(largest)
    return new[:k]
