def remove_extras(lst):
    lst1 = lst.reverse
    for i in lst:
        if lst.count(i) >1:
            lst1.remove(i) * (i-1)
    return lst1.reverse
