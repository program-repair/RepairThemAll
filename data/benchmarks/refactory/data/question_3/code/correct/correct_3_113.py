def remove_extras(lst):
    non_extra = ()
    count = 0
    for el in lst:
        if el not in non_extra:
            non_extra += (el,)
        else:
           continue 
    lst = list(non_extra)
    return lst
