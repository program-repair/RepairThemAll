def remove_extras(lst):
    for i in lst:
        if lst.count(i)>1:
            lst=lst.reverse()
            lst=lst.remove(i)
            lst=lst.reverse
    return lst
