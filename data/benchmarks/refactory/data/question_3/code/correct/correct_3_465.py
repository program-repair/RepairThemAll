def remove_extras(lst):
    a =[]
    for i in lst:
        if i not in a:
            a = a + [i,]
        else:
            continue
    return a
    pass
