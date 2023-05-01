def remove_extras(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res
