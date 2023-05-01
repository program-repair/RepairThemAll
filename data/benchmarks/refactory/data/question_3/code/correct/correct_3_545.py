def remove_extras(lst):
    t=[]
    for i in lst:
        if i not in t:
            t.append(i)
        else:
            pass
    return t
