
def remove_extras(lst):
    x = []
    for i in lst:
        if i not in x:
            x = x + [i,]
        else:
            continue
    return x
