def remove_extras(lst):
    for k in range(len(lst)):
        if lst[k] in lst[:k]:
            return lst.remove(lst[k])
        else:
            return lst
