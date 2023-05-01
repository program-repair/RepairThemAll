def remove_extras(lst):
    newlst = []
    for i in lst:
        if i not in newlst:
            newlst += [i]
    return newlst 
