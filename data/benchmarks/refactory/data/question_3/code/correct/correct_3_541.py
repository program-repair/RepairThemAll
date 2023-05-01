def remove_extras(lst):
    new = []
    for e in lst:
        if e not in new:
            new.append(e)
    return new
