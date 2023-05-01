def remove_extras(lst):
    for elem in lst:
        while elem in lst[lst.index(elem)+1:]:
            lst.remove(elem)
    return lst
            
