def top_k(lst, k):
    
    
    newlist = []
    counter = k
    
    while counter > 0:
        biggest = lst[0]
        for i in lst[1:]:
            if biggest > i:
                continue
            else:
                biggest = i
                continue
    
        newlist += [biggest]
        counter -= 1
        lst.remove(biggest)
        
    return newlist

    
