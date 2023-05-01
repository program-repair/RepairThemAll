def remove_extras(lst):
    i=1
    while i!=len(lst):
        if lst[i] in lst[:i]:
            del lst[i]
            continue
        i+=1
    return lst
