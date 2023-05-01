def remove_extras(lst):
    new = []
    for x in lst:
        if x not in new:
            new += [x]
    return new
    
