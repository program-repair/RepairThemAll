def remove_extras(lst):
    i = 0
    while i < len(lst):
        if lst[0] in lst[1:]:
            lst.remove(lst[0])
        i = i + 1
    return lst

