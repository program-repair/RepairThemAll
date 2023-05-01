def remove_extras(lst):
    for k in range(len(lst)):
        if lst[k] in lst[:k]:
            return lst[:k] + lst[k+1:]
        else:
            return lst
