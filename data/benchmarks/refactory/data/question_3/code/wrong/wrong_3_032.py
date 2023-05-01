def remove_extras(lst):
    for i in lst:
        if i not in sumx:
            sumx.append(i)
    return sumx
