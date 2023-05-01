def remove_extras(lst):
    s = []
    for element in lst:
        if element not in s:
            s.append(element)
    return s
