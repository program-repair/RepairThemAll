def remove_extras(lst):
    check=True
    lst1=[]
    for i in lst:
        for j in lst1:
            if j==i:
                check=False
        if check:
            lst1+=[i,]
    return lst1
