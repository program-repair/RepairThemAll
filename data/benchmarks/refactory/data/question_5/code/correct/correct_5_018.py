def top_k(lst, k):
    if lst==[]:
        return []
    sort=[]
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        sort.append(largest)
    return sort[:k]
    pass
