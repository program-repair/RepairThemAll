def remove_extras(lst):
    newlist = []
    for i in lst:
        if i in newlist:
            continue
        else:
            newlist += [i]
    return newlist
