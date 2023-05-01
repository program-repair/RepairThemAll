def remove_extras(lst):
    newlst=[]
    for i in lst:
        while i not in newlst:
            newlst.append(i)
    return newlst
