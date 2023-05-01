def top_k(lst, k):
    sort = []
    if k==0 or lst==[]:
        return []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
                
        lst.remove(biggest)
        sort.append(biggest)
        if len(sort)==k:
            break
    return sort
