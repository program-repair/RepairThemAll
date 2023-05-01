def remove_extras(lst):
    for i in range (len(lst)-1):
        for j in lst[i+1:]:
            if j==lst[i]:
                lst.remove(j)
    return lst
