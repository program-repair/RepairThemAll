def remove_extras(lst):
    new_list=[lst[0]]
    for i in lst:
        if i in new_list == True:
            continue
        else:
            new_list.append(i)
    return new_list
