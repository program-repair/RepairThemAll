def sort_age(lst):
    first = lst[0]
    firstnum = lst[0][1]
    result = []
    for x in lst[1:]:
        if x[1] > firstnum:
            result = (first,) + (x,)
        else:
            result = (x,) + (first,)
    return result
    pass
