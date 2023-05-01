def top_k(lst, k):
    sort = []
    while lst:
        largest = lst[0]
        for e in lst:
            if e > largest:
                largest = e
        lst.remove(largest)
        sort.append(largest)
    return sort[:k]
        
