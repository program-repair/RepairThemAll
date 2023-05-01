def top_k(lst, k):
    a = []
    while k > 0:
        a.append(max(lst))
        lst.remove(max(lst))
        k -= 1
    return a
    
