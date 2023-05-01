def top_k(lst, k):
    lst2 = []
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
        lst.pop(max)
        while len(lst2) != k:
            lst2.append(max)
    return lst2
