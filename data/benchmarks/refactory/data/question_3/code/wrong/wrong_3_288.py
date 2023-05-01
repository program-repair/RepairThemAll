def remove_extras(lst):
    new = []
    for i in lst:
        for j in i:
            if j != i:
                new.append(j)
    return new
