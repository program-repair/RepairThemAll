def top_k(lst, k):
    result = []
    for i in range(k):
        result.append(max(lst))
        lst.remove(max(lst))
    return result
        
