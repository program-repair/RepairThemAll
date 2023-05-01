def remove_extras(lst):
    a =[lst[0]]
    i = lst[0]
    for j in range (1,len(lst)): #while lst is not empty 
        if i == lst[j]:
            continue
        else: 
            a += [lst[j]]
    
    return a 
