def top_k(lst, k):
    sort = []
    while lst:
        oldest = lst[0]
        for x in lst:
            if x > oldest:
                oldest = x
        lst.remove(oldest)
        sort.append(oldest)
    return sort[0:k]
    
