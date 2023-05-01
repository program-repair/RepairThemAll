def remove_extras(lst):
    newlst = []
    [newlst.append(i) for i in lst if i not in newlst]
    return newlst
