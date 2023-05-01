def remove_extras(lst):
    newLst=[]
    for i in lst:
        if i not in newLst:
            newLst.append(i)
        else:
            continue
    return newLst
