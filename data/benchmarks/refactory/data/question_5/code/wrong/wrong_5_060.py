def top_k(lst, k):
    new_lst = []
    while lst:
        biggest = lst[0]
        for x in lst:
            if x < lst[0]:
                biggest = x
        lst.remove(biggest)
        new_lst.append(biggest)
    return new_lst[0:k]
    
