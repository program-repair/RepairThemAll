def remove_extras(lst):
    new_list = []
    for x in lst:
        if (x in new_list) == False:
            new_list.append(x)
    return new_list
