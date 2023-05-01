def top_k(lst, k):
    new = []
    for i in range(k):
        top = max(lst) 
        new.append(top)
        lst.remove(top)
        
    return new
        
