def remove_extras(lst):
    o = []
    for i in lst:
        if i not in o:
            lst.remove(i)
            o.append(i)
    return o
