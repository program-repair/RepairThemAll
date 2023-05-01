def remove_extras(lst):
    lst_new = list()
    for i in lst:
        if (i in lst_new):
            continue
        else:
            lst_new.append(i)
    return lst_new
