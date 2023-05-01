def top_k(lst, k):
    lst2 = []
    lst3 = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        lst2.append(largest)
    if len(lst2) <= k:
        k = len(lst2)
    for i2 in range(k):
        lst3.append(lst2[i2])
    return lst3    
