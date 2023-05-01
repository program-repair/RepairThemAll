def remove_extras(lst):
    new = []
    for term in lst:
        if term not in new:
            new += [term,]
    return new
                    
