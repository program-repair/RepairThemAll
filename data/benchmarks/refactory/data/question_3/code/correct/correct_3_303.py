def remove_extras(lst):
    new_list = []
    for item in lst:
        if new_list.count(item) == 0:
            new_list.append(item)
    return new_list
