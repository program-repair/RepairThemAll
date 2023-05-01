def remove_extras(lst):
    lst.reverse()
    for element in lst:
        if lst.count(element)>1:
            lst.remove(element)
    return lst.reverse()
