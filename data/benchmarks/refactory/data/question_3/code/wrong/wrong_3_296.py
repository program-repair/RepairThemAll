def remove_extras(lst):
    new = []
    x = 0
    while x < len(lst)+1:
        if lst[x] in new:
            new += lst[x]
        else:
            continue
    return new
