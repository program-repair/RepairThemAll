def remove_extras(lst):
    new_lst = [lst[0],]
    for e in lst:
        if e in new_lst:
            continue
        else:
            new_lst.append(e)
            
    return new_lst
    
    
    
