def remove_extras(lst):
    new = []
    x = 0
    for x in range(len(lst)):
        if lst[x] not in new:
            new += [lst[x]]
    return new
