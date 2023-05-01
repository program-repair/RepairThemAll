def sort_age(lst):
    firstnum = lst[0][1]
    result = (lst[0],)
    for x in lst[1:]:
        if x[1] < firstnum:
            result += (x,)
        else:
            result = (x,) + result
    return result
    pass
