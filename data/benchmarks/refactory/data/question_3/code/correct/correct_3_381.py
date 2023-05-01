def remove_extras(lst):
    newlst = []
    for i in lst:
        if i in newlst:
            continue
        newlst.append(i)
    return newlst
