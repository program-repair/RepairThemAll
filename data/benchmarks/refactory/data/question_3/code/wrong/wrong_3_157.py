def remove_extras(lst):
    for i in lst:
        test_lst = lst.remove(i)
        if i not in test_lst:
            continue
        else:
            lst = lst.remove(i)
    return lst
