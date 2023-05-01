def remove_extras(lst):
    new_list = []
    for elem in lst:
        if elem not in new_list:
            new_list.append(elem)
    return new_list 
