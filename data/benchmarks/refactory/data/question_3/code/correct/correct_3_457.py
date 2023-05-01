def remove_extras(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst += [lst[i]]
    return new_lst
