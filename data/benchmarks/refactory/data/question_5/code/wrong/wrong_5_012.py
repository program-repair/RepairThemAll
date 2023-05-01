def top_k(lst, k):
    
    if lst == []:
        return lst
    
    lower = []
    higher = []
    plist = []
    
    pivot = lst[0]
    for e in lst:
        if e < pivot:
            lower.append(e)
        if x == pivot:
            plist.append(e)
        if x > pivot:
            higher.append(e)
    sort_list = lower + plist + higher
    
    return sort_list[:k]
