def top_k(lst, k):
    results = []
    for i in range(k):
        results.append(max(lst))
        lst.remove(max(lst))
    return results
        
    
