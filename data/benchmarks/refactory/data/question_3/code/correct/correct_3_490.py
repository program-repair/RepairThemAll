def remove_extras(lst):
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2
