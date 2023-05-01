def remove_extras(lst):
    for i in lst:
        for j in lst[0:i]:
            if i == j:
                remove.lst(lst[i])
            else:
                continue
    return lst
    pass
