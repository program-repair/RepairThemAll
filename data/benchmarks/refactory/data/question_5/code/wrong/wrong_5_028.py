def top_k(lst, k):
    sort = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        sort.append(i)
    return sort[:k-1]
        
