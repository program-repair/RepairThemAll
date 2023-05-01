def top_k(lst, k):
    new = []
    for i in range(k-1):
        new.append(lst.pop(max(lst)))
        
    return new
        
