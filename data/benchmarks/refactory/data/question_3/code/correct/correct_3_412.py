def remove_extras(lst):
    lst1 = []
    for item in lst:
        if (item in lst1):
            continue
        else:
            lst1 += [item,]
    return lst1
