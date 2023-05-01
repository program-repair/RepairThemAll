def remove_extras(lst):
    new_lst=[]
    for x in lst:
        if x in new_lst:
            continue
        else:
            new_lst+=[x,]
    return new_lst
