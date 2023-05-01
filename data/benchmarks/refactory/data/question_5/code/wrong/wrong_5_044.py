def top_k(lst, k):
    af_sort = []
    while lst:
        biggest = lst[0] 
        for element in a:
            if element > biggest:
                biggest = element
            lst.remove(biggest)
            af_sort.append(biggest)
    return af_sort[0:k]
    
