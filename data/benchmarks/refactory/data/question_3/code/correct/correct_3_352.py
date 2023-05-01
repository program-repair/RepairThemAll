def remove_extras(lst):
    rem_lst=[]
    for i in lst:
        if rem_lst.count(i)==0:
            rem_lst+=[i]
    return rem_lst
