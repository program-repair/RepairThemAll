def remove_extras(lst):
    new = []
    for i in lst:
        if i not in new:
            new = new + [i,]
        else:
            new = new
    return new
