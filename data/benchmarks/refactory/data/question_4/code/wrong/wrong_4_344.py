def sort_age(lst):
    current=0
    tup=()
    for i in lst:
        if i[1]>current:
            tup+=tuple(i)
            current=i[1]
        else:
            tuple(i)+tup
    return tup
            
