def remove_extras(lst):
    new_list = []
    n = len(lst)
    for counter1 in range(n):
        if lst[counter1] not in new_list:
            new_list.append(lst[counter1])
    return new_list
                
