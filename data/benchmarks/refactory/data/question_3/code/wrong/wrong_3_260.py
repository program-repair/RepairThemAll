def remove_extras(lst):
    for element in lst:
        if count(element) > 1:
            lst.remove(element)
    return lst
