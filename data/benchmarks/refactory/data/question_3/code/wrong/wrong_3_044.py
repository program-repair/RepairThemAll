def remove_extras(lst):
    new_lst = []
    for i in lst:
        if i == lst[i+1]:
            continue
        else:
            new_list += i
    return new_lst
            
        
