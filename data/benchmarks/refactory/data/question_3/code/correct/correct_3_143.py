def remove_extras(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1 += [i,]
    return lst1
