def remove_extras(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            lst.pop(i)
    return lst
