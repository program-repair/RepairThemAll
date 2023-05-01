def top_k(lst, k):
    l = []
    if k > len(lst):
        return False
    elif k == 1:
        return lst
    else:
        while len(l) <= k:
            a = max(lst)
            lst.remove(a)
            l.append(a)
        
        return l
        
    # Fill in your code here
    pass
