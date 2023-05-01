def top_k(lst, k):
    x = []
    for i in range(k-1):
        y = i
        for j in lst:
            if y < j:
                y = j
        x += y
    return x    
                
                
    
    pass
