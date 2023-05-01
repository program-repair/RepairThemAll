def remove_extras(lst):
    new_lst = []
    for x in lst:
        if x not in new_lst:
            new_lst += [x]
    return lst
