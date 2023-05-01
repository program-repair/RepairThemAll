def remove_extras(lst):
    pst=[]
    for i in lst:
        if i not in pst:
            pst.extend(list(i))
    return pst
