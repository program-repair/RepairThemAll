def remove_extras(lst):
    if lst == []:
        return []
    else:
        lst1 = []
        for i in range(0,len(lst)):
            if lst[i] not in lst1:
                lst1 = lst1 + [lst[i]]
        return lst1
