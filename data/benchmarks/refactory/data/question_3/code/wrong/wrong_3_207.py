def remove_extras(lst):
    lst.sort()
    i = 1
    n = len(lst)
    while i < n:
        if lst[i]==lst[i-1]:
            lst.remove(i)
        else:
            i += 1
        n = len(lst)
    return lst
    pass
