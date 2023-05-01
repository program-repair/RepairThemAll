def top_k(lst, k):
    new = []
    while len(lst) >= len(lst) - k:
        top = max(lst) 
        new.append(lst.remove(top))
        
    return new
        
