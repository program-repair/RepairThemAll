def remove_extras(lst):
    a = []
    for ele in lst:
        if ele in a:
            continue
        else:
            a = a+[ele]
    return a
