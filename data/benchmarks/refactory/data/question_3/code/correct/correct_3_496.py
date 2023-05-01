def remove_extras(lst):
    s = []
    for i in lst:
        if i not in s:
            s.append(i)
    return s
