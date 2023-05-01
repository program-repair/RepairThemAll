def remove_extras(lst):
    l=[]
    for i in lst:
        checker=True
        for k in l:
            if k==i:
                checker=False
        if checker:
            l+=[i]
    return l
