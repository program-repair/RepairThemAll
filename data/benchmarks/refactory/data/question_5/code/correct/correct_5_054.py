def top_k(lst, k):
    
    answer = []
    a = lst[0]
    
    while lst:
        
        for i in range(len(lst)):
            answer.append(max(lst))
            lst.remove(max(lst))
            
    return answer[:k]

