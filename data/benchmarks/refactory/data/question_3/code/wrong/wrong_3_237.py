def remove_extras(lst):
    l=len(lst)
    for i in l:
        for j in range(i+1,l):
            if lst[i]==lst[j]:
                del lst[j]
    return lst

