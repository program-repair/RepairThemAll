def remove_extras(lst):
    new_lst = []
    for ele in lst:
        if ele in new_lst:
            continue
        else:
            new_lst += [ele]
    return new_lst
