def remove_extras(lst):
    for i in lst:
        if lst.count(i) > 1:
            left = lst[:lst.index(i)+1]
            right = lst[lst.index(i)+1:]
            right.remove(i)
            lst = left + right
    return lst
