def remove_extras(lst):
    new_lst=[]
    for element in lst:
        if element not in new_lst:
            new_lst += [element]
    return new_lst
