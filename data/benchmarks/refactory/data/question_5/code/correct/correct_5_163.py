def top_k(lst, k):
    n= []
    while lst:
        big = lst[0]
        for ele in lst:
            if ele>big:
                big = ele
        if len(n)==k:
            break 
        else:
            n.append(big)
            lst.remove(big)
    return n
        
                
    
    pass
