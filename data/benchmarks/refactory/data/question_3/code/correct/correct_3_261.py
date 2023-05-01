def remove_extras(lst):
    new_list = []
    for k in range(len(lst)):
        if lst[k] in lst[:k]:
            new_list = new_list
        else:
            new_list = new_list + [lst[k]]
    return new_list 
