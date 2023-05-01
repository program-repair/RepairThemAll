def remove_extras(lst):
    new_lst = []
    for element in lst:
        if element in new_lst:
            continue
        else:
            new_lst += [element]
    return new_lst
