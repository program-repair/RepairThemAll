def remove_extras(lst):
    result = []
    counter = 0
    while counter < len(lst):
        for i in lst[1:]:
            if lst[counter] == i:
                lst = lst.append(i)
    return lst
