def top_k(lst, k):
    l = []
    if k > len(lst):
        return False
    elif k == 1:
        return lst
    else:
        a = max(lst)
        lst.remove(a)
        l.append(a)
        top_k(lst, k-1)
        return l
        
    # Fill in your code here
    pass
