def remove_extras(lst):
    for i in range(0, len(lst)-1):
        if lst.count(lst[i]) > 1:
            lst.pop(i)
    return lst
