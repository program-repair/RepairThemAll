def remove_extras(lst):
    lst.sort()
    i = len(lst)-1
    while i > 0:  
        if lst[i]==lst[i - 1]:
            lst.pop(i)
        i-=1
    return lst
