def top_k(lst, k):
    sorted_lst = []
    while lst:
        for n in range(1, len(lst)):
            biggest = lst[0]
            if lst[n] >= biggest:
                biggest = lst[n]
                lst.remove(biggest)
                sorted_lst.append(biggest)
    return sorted_lst[0:k]
            
            
