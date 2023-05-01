def remove_extras(lst):
    copy_list = lst.copy()
    copy_list.reverse()
    for i in lst:
        x = lst.count(i)
        if x > 1:
            for j in range(x-1):
                copy_list.remove(i)
            lst = copy_list
            lst.reverse()
    return lst
