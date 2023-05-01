def top_k(lst, k):
    result = []
    length=len(lst)
    while len(lst)>length-k:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        result.append(biggest)
        lst.remove(biggest)
        
    return result
    pass
