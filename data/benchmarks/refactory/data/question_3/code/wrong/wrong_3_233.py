def remove_extras(lst):
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            lst.append(i)
    return new_lst
