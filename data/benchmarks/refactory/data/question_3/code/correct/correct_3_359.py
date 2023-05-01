def remove_extras(lst):
    res= []
    for i in lst:
        if res.count(i) == 0:
            res = res + [i]
        else:
            res = res
    return res
