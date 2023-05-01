def remove_extras(lst):
    # your code here
    for item in st:
        while lst.count(item) != 1:
            lst.pop(item)
    return lst
