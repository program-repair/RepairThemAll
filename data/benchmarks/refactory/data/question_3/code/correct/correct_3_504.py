def remove_extras(lst):
    newlst = []
    while len(lst) > 0:
        x = lst[0]
        newlst.append(x)
        lst.remove(x)
        while x in lst:
            lst.remove(x)                
    return newlst
