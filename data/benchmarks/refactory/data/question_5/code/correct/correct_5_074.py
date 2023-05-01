def top_k(lst, k):
    a = lst.copy()
    b = lst.copy()
    lst.clear()
    for i in range(len(b)):
        lst.append(max(a))
        a.remove(max(a))
    lst = lst[:k]
    return lst# Fill in your code here
    pass
