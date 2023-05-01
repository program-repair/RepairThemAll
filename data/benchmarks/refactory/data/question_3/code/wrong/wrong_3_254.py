def remove_extras(lst):
    new_lst = []
    if lst == []:
        return new_lst
    elif lst[0] in new_lst:
        return new_lst + remove_extras(lst[1:])
    else:
        new_lst += [lst[0]]
        return new_lst + remove_extras(lst[1:])
