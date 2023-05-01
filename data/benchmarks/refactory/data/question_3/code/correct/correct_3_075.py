def remove_extras(lst):
    for i in lst:
        remove_multiple(i, lst)
    return lst
    
    

    
def remove_multiple(n, lst):
    if lst.count(n) == 1:
        return lst
    else:
        lst.reverse()
        lst.remove(n)
        lst.reverse()
        return remove_multiple(n, lst)
