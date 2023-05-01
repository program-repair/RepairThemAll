def remove_extras(lst):
    i=0
    new = []
    while i<=len(lst):    
        curr = lst[i]
        for ele in lst:
            if ele == curr:
                continue
            new += [ele,]
        lst = new.copy()
        new = []
        i +=1
    return lst    
    
