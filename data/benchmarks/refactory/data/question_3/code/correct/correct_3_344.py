def remove_extras(lst):
    newlst = []
    for elem in lst:
        if elem not in newlst:
            newlst.append(elem)
    return newlst
