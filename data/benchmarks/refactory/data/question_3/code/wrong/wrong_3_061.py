def remove_extras(lst):
    o = []
    for i in lst:
        if i not in o:
            o.append(lst.pop(i))
    return o
