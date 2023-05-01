def remove_extras(list):
    list.reverse()
    for element in list:
        if list.count(element)>1:
            list.remove(element)
    list.reverse()
    return list
