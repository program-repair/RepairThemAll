def top_k(lst, k):
    new = []
    while len(lst) > len(lst) - k:
        top = max(lst) 
        new.append(top)
        lst.remove(top)
        
    return new
        
