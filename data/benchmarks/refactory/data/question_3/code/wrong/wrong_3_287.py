def remove_extras(lst):
    for element in lst:
        while lst.count(element) > 1:
            lst.remove(element)
            if  lst.count(element) == 1:
                break
        return lst
