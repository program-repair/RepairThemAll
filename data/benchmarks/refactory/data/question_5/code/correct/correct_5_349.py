def top_k(lst, k):
    list = []
    while len(list) < k:
        a = max(lst)
        lst.remove(a)
        list.append(a)
    return list
