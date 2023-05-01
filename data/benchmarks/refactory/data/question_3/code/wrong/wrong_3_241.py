def remove_extras(lst):
    new_lst = []
    if lst == []:
        return new_lst
    elif lst[0] not in lst:
        new_lst += lst[0] + remove_extras(lst[1:])
    else:
        new_lst += remove_extras(lst[1:])
