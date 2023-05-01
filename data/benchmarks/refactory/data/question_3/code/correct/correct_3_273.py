def remove_extras(lst):
    t = []
    for n in lst:
        if t.count(n) == 0:
            t = t + [n,]
    return t
