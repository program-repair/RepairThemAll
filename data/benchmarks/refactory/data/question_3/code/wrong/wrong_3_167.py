def remove_extras(lst):
    newlst = lst(0)
    for i in lst:
        if i not in newlst:
            newlst += [i]
    return newlst    
