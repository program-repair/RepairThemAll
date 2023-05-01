def remove_extras(lst):
    new = []
    for i in range(len(lst)):
        if lst[i] not in new:
            new.append(lst[i])
    return new
