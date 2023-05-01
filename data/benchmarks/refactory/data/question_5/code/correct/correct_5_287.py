def top_k(lst, k):


    while True:
        changed = False
        for i in range(len(lst)-1):
            if lst[i+1]>lst[i]:
                lst[i],lst[i+1] = lst[i+1], lst[i]
                changed = True
        if not changed:
            break
    
    while len(lst)>k:
        if len(lst)<=k:
            return lst
        else:
            lst.pop(k)
    
    return (lst)
