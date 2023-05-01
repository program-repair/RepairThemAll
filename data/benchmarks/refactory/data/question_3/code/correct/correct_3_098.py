def remove_extras(lst):
    l=[]
    for x in lst:
        if x not in l:
            l.append(x)
    return l
