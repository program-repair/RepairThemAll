def sort_age(lst):
    first = lst[0][1]
    result = []
    for x in lst[1:]:
        if x[1] > first:
            result = (first,) + (x[1],)
        else:
            result = (x[1],) + (first,)
    pass
