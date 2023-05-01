def remove_extras(lst):
    lst2 = []
    for x in lst:
        if lst.count(x) < 1:
            lst2.append(x)
    return lst2
