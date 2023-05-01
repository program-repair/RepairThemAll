def top_k(lst, k):
    sort = []
    counter = 0
    while counter != k:
        sort.append(max(lst))
        lst.remove(max(lst))
        counter += 1
    return sort
