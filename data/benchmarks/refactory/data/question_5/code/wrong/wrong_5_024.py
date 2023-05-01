def top_k(lst, k):
    sort = []
    while lst:
        biggest = lst[0]
        for i in lst[1:]:
            if i > biggest:
                oldest = i
        lst.remove(biggest)
        sort.append(biggest)
    
    n = 1
    sort_k = []
    while n <= k:
        sort_k.append(sort.pop[0])
        n += 1
    
    return sort_k
        
