def remove_extras(lst):
    for i in lst:
        if lst.count(i)>1:
            lst.remove(i)
    return lst
