def top_k(lst, k):
    new = []
    while len(lst) > len(lst) - k:
        new.append(lst.pop(max(lst)))
        
    return new
        
