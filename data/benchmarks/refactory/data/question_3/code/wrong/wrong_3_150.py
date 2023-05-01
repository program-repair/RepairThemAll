def remove_extras(lst):
    for i in range(1,len(lst)):
        if i in lst[i:]:
            lst = lst.remove(i)
    return lst
