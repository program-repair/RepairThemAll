def remove_extras(lst):
    seq = (lst[0],)
    for i in lst:
        if i not in seq:
            seq = seq + (lst[i],)
    return seq
    pass
