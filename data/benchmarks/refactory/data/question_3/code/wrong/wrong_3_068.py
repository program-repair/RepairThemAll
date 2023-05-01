def remove_extras(lst):
    extra = []
    for i in lst:
        if i not in lst:
            continue
        else:
            extra += i
    return lst.remove(int(extra))
