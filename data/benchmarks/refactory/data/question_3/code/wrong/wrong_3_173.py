def remove_extras(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst[1:])):
            if lst[i] == lst[j]:
                del lst[j]
    return lst
                
