def remove_extras(lst):
    tmp = []
    for x in lst:
        if x not in tmp:
            tmp.append(x)
    return tmp
