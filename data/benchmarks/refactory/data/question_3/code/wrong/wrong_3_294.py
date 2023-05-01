def remove_extras(lst):
    keep = []
    destroy = []
    for i in lst :
        if i not in keep :
            keep.append(i)
        elif i in keep :
            destroy.append(i)
    for i in destroy :
        lst.remove(i)
    return lst
