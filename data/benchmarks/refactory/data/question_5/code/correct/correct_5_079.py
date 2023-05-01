def top_k(lst, k):
    new = []
    for i in range(k):
        largest = max(lst)
        new += [largest]
        lst.remove(largest)
    return new
