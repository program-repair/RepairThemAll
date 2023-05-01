def sort_age(lst):
    total = ()
    def helper(i, tup):
        if tup == ():
            return (i,)
        elif i[1] > tup[0][1]:
            return (i,)+ tup
        else:
            return (tup[0],) + helper(i, tup[1:])
    for i in lst:
        if total == ():
            total = (i,)
        else:
            total = helper(i, total)
    return list(total)
