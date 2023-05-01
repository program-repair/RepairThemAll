def remove_extras(lst):
    keep = []
    for i in lst :
        if i not in keep :
            keep.append(i)
    return lst
