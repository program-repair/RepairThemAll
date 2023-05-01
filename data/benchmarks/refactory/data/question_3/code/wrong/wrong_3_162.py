def remove_extras(lst):
    newlst = []
    for i in lst:
        if i not in lst:
            newlst.append(i)
    return newlst
