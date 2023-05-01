def top_k(lst, k):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    result = []
    for i in range(k):
        result.append(lst[i])
    return result
    
           
        
