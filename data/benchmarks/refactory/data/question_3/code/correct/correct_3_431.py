def remove_extras(lst):
    n = 0
    while n < len(lst):
        if lst[n] in lst[n+1:]:
            ext = lst[n+1:]
            ext.remove(lst[n])
            lst = lst[:n+1] + ext
        else:
            n = n + 1
    return lst
        
        
        
        
