def remove_extras(lst):
    i=0
    while i<len(lst):    
        curr = lst[i]
        new = []
        for ele in lst:
            if ele == curr:
                continue
            new += [ele,]
        lst = new.copy
        i +=1
