def remove_extras(lst):
    newlist = []
    for i in lst:
        if i not in newlist:
            newlist = newlist + [i,]
    return newlist
    

"""    
    if lst == []:
        return []
    elif lst[0] not in lst[1:]:
        return [lst[0],] + remove_extras(lst[1:])
    else:
        return remove_extras(lst[1:])
"""
