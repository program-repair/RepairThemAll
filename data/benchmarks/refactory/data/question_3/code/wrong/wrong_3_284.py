def remove_extras(lst):
    for x in range(len(lst)):
        if lst[x] in lst[:x] or lst[x] in ls[x+1:]:
            lst.remove(lst[x])
    return lst
