def remove_extras(seq):
    new_lst = []
    for i in seq:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
