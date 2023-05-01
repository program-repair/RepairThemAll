def remove_extras(lst):
    empty_list = []
    for i in lst:
        if i not in empty_list:
            empty_list += [i]
    return empty_list
    pass
