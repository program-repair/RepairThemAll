def remove_extras(lst):
    for i in range(len(lst)-1):
        if lst[i] in lst[:i]+lst[i+1:]:
            lst.pop(i)
    return lst
        
