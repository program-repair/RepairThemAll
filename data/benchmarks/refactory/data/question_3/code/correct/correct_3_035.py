def remove_extras(lst):
    newlist = []
    for x in lst:
        if x not in newlist:
            newlist.append(x)
    return newlist
