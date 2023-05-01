def remove_extras(lst):
    lst2 = []
    for x in lst:
        if x not in lst2:
            lst2.append(x)
    return lst2
