def remove_extras(lst):
    lst.sort()
    i = 0
    while i <len(lst)-1:
        if lst[i+1] == lst[i]:
            lst.remove(lst[i])
        else:
            i += 1
    return lst
