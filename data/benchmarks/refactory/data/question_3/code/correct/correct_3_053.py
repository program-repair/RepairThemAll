def remove_extras(lst):
    new = []
    for el in lst:
        if el not in new:
            new += [el,]
    return new
