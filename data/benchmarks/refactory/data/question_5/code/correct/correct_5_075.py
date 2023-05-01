def top_k(lst, k):
    sort = []
    i = 0
    while i < k:
        smallest = lst[0]
        for element in lst:
            if element > smallest:
                smallest = element
        lst.remove(smallest)
        sort.append(smallest)
        i += 1
       
    return sort 
