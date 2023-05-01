def remove_extras(lst):
    lst.reverse()
    if lst[0] in lst[1:]:
        lst.pop(0)
    lst.reverse()
    return lst
