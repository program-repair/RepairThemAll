def top_k(lst, k):
    sort = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        sort.append(largest)
    print(sort)
    return sort[:k]
        
