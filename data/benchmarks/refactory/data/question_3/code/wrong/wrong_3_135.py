def remove_extras(lst):
    i = -1
    while i >= (-len(lst)):
        if lst[i] in lst[:-1]:
            lst.pop(i)
    i = i - 1
    return lst
