def remove_extras(lst):
    remove_lst = []
    for i in lst:
        if i not in lst:
            remove_lst.append(i)
    return remove_lst
