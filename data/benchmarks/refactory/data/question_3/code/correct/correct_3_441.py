def remove_extras(lst):
    i=0
    new = []
    while i<=len(lst)-1:    
        curr = lst[i]
        new += [curr,]
        for ele in lst:
            if ele == curr:
                continue
            new += [ele,]
        lst = new.copy()
        new = []
        i +=1
    lst.reverse()
    return lst
