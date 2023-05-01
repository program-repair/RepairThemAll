def remove_extras(lst):
    new_list = []
    for element in lst:
        if element in new_list:
            continue
        else:
            new_list += new_list.append(element)
