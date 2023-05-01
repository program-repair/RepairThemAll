def remove_extras(lst):
    new_lst = []
    for i in lst:
        if i in new_lst:
            new_lst = new_lst
        else:
            new_lst += [i]
    return new_lst
