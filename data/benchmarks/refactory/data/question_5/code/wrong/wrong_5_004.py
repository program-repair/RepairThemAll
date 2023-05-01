def top_k(lst, k):
    sort = []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if ele > biggest:
                biggest = ele
                
        lst.remove(element)
        sort.append(element)
        if len(sort)==k:
            break
    return sort
