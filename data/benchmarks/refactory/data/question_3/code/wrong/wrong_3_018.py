def remove_extras(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] == lst[i]:
                lst = lst[:j] + lst[j+1:]
    return lst
    
