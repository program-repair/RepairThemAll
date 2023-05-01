def sort_age(lst):
    current=0
    tup=[]
    for i in lst:
        if i[1]>current:
            tup.append(i)
        else:
            i.append(tup)
    return tup
            
