def remove_extras(lst):
    new = []
    for i in lst:
        if i not in new: #if its already in new, it would skip the element and wont add into the new listt.
            new += [i, ]
        else:
            continue
    return new
        

