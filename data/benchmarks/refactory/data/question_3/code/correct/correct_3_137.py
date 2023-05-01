def remove_extras(lst):
    new_lst=[]
    for i in lst:
        if i in new_lst:
            continue
        else:
            new_lst.append(i)
    return new_lst
            
    
 
