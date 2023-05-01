def remove_extras(lst):
    newlst = []
    for element in lst:
        if element not in newlst:
            newlst = newlst + [element]
    return newlst
