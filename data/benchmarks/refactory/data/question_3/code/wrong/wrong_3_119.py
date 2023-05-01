def remove_extras(lst):
    new_lst = []
    for ele in lst:
        if ele not in new_lst:
            new_lst += ele
    return new_lst
