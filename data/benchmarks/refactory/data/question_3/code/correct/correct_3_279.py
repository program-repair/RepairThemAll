def remove_extras(lst):
    # your code here
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst += [i,]
    return new_lst
        
