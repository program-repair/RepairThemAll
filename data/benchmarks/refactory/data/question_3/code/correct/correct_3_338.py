def remove_extras(lst):
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    return l 
