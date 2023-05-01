def remove_extras(lst):
    for element in lst:
        if lst.count(element) > 1:
            lst.remove(element)
    return lst
