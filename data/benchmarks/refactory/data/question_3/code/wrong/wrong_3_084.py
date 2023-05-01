def remove_extras(lst):
    if lst == []:
        return []
    elif lst[0] not in lst[1:]:
        return lst[0] + remove_extras(lst[1:])
    else:
        return remove_extras(lst[1:])
            
