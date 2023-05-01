def remove_extras(lst):
    
    seq = []
    
    for i in lst:
        if i in seq:
            continue
        else:
            seq += [i]
    
    return seq
