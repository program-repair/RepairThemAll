def remove_extras(lst):
    for num in lst:
        while lst.count(num)>1:
            lst.remove(num)
    return lst
