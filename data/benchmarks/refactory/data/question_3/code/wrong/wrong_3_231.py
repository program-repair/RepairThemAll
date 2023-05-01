def remove_extras(lst):
    lst = []
    for i in lst:
        if lst.count(i) == 1:
            lst += i
        
    return lst
