def remove_extras(lst):

    lst1=[]
    for i in lst:
        check=True
        for j in lst1:

            if j==i:
                check=False
        if check:
            lst1+=[i,]
    return lst1
