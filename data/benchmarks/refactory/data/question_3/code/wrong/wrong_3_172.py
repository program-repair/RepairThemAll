def remove_extras(lst):
    for i in range(len(lst)):
        for j in range(len(lst[1:])):
            if lst[i] == lst[j]:
                del lst[j]
    return lst
                
