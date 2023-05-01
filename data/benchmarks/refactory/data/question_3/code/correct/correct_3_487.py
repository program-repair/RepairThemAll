def remove_extras(lst):
    lst_new=[]
    for i in range (len(lst)):
        if lst[i] in lst_new:
            continue
        else:
            lst_new.append(lst[i])
    return lst_new
