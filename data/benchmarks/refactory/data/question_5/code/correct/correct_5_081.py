def top_k(lst, k):
    # Fill in your code here
    new = []
    for i in range(k):
        a = max(lst)
        lst.remove(a)
        new.append(a)
    return new
        
