def remove_extras(lst):
    lst_new=[]
    l=len(lst)
    for i in range (l):
        if lst[i] in lst_new:
            continue
        else:
            lst_new.append(lst[i])
    return lst_new

