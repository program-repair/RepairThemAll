def top_k(lst, k):
    result = []
    
    while len(lst)>len(lst)-k:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        result.append(biggest)
        lst.remove(biggest)
        
    return result
    pass
