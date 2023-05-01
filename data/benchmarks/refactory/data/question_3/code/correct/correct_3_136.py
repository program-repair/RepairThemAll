def remove_extras(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst = new_lst + [i,]
        else:
            continue
    return new_lst
    
