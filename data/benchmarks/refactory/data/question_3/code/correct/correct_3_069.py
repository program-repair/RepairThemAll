def remove_extras(lst):
    list1 = []
    for i in lst:
        if i not in list1:
            list1 += [i,]
    return list1
