def top_k(lst, k):
    lst2 = []

    while lst:
        lst2.append(max(lst))
        lst.remove(max(lst))
        for x in lst:
            if x in lst2:
                lst2.append(x)
                lst.remove(x)
    return lst2[:k]
