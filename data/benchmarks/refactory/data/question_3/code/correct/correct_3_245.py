def remove_extras(lst):
    # your code here
    z=[]
    for i in lst:
        if i in z:
            continue
        else:
            z.append(i)
    return z

