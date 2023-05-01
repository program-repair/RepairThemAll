def remove_extras(lst):
    if lst==[]:
        return []
    new_list=[lst[0]]
    for i in lst:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list
