def remove_extras(lst):
    lst1 = lst.reverse
    for i in lst:
        if lst.count(i) >1:
            j = 0
            while j < i:
                lst1.remove(i)
                j += 1
    return lst1.reverse
