def remove_extras(lst):
    a = []
    for repeat in range(len(lst) + 1):
        if repeat not in a:
            a += [repeat,]
    return a
        
        
