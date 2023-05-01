def top_k(lst, k):
    # Fill in your code here
    a = []
    while len(a)<k:
        a += [max(lst),]
        lst.remove(max(lst))
    return a 
        
