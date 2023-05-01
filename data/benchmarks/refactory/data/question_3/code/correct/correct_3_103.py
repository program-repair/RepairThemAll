def remove_extras(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[0] in new_lst:
            new_lst = new_lst
            lst = lst[1:]
        else:
            new_lst.append(lst[0])
            lst = lst[1:]
    return new_lst
