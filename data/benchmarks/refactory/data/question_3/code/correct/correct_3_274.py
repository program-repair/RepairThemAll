def remove_extras(lst):
    newlst = []
    for item in lst:
        if item not in newlst:
            newlst.append(item)
    return newlst
