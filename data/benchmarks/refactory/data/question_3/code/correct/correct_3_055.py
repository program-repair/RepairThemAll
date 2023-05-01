def remove_extras(lst):
    lst.reverse()
    for i in lst:
        if lst.count(i) >1:
            j = 0
            while j < lst.count(i):
                lst.remove(i)
                j += 1
    lst.reverse()
    return lst
