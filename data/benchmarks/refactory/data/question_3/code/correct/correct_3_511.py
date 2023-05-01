def remove_extras(lst):
    new = []
    for i in lst:
        if i not in new:
            new.append(i)
        else:
            new = new
    return new
