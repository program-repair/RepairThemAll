def top_k(lst, k):
    while lst:
        maximum=[]
        for a in range(len(lst)):
            maximum.append(max(lst))
            lst.remove(max(lst))
            
    return maximum[0:k]
