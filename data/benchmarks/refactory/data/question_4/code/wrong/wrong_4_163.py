def sort_age(lst):
    lst = ()
    for i in lst:
        if lst[i][1]<lst[0][1]:
            lst += lst[0]
        else:
            lst += lst[i]
    return lst
