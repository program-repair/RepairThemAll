def remove_extras(lst):
    i = 0
    while i < len(lst):
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j]:
                lst = lst[:j] + lst[j+1:]
        i += 1
    return lst
    
