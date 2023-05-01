def remove_extras(lst):
    list = []
    for element in lst:
        if element not in list: 
            list.append(element)
        else:
            continue
    return list
