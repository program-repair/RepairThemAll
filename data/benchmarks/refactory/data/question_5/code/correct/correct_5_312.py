def top_k(lst, k):
    for start in range(len(lst)):
        minimum = start
        for i in range(start,len(lst)):    
            if lst[i] < lst[minimum]:
                minimum = i
        lst[start], lst[minimum] = lst[minimum], lst[start]
    lst.reverse()            
    return lst[:k]
