def top_k(lst, k):
    a=[]
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        a.append(largest)
    return a[:k]
