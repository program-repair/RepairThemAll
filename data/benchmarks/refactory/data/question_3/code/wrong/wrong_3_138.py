def remove_extras(lst):
    lst1 = []
    for i in range(len(lst)):
        if lst[i] in lst1:
            lst1.remove(lst[i])
            return lst1
        else:
            return []
