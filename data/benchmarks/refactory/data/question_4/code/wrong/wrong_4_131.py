def sort(lst):
    for i in range(len(lst)-1):
        if lst[i][1] > lst[i+1][1]:
            temp = lst[i]
            del lst[i]
            lst += [temp]
        else:
            continue
    return lst

def sort_age(lst):
    oldlist = tuple(lst)
    if tuple(sort(lst)) == oldlist:
        return lst
    else:
        sort(lst)
        return sort_age(lst)
