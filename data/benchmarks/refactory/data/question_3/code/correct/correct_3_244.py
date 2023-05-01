def remove_extras(lst):
    # your code here
    lst.reverse()
    for item in lst:
        while lst.count(item) != 1:
            lst.remove(item)
    lst.reverse()
    return lst

