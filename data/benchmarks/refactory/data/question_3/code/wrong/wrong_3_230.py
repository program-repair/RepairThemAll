def remove_extras(lst):
    new_lst = []
    for i in lst:
        if i not in lst[i:]:
            new_lst = new_lst.append(i)
    return new_lst
        
    pass
