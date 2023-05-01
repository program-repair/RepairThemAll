def remove_extras(lst):
    remove_indices = []
    
    for i in range(len(lst)):
        this = lst[i]
        
        for j in range(i):
            if lst[j] == this:
                remove_indices.append(i)
            
    for i in remove_indices:
        lst[i] = None
        
    while None in lst:
        del lst[lst.index(None)]
    
    return lst
