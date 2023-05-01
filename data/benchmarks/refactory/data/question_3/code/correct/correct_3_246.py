
def remove_extras(lst):
    s =[]
    for i in lst:
        if i not in s:
            s = s +[i]
    lst.clear()
    lst.extend(s)
    return lst
