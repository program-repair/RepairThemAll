def remove_extras(lst):
    a = []
    for i in lst:
        if i in a:
            continue
        else:
            a.append(i)
    return a
    
