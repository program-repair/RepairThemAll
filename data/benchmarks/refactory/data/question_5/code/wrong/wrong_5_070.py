def top_k(lst, k):
    new = []
    while len(lst) > len(lst) - k:
        new.append(lst.remove(max(lst)))
        
    return new
        
