def remove_extras(lst):
    new_lst=[]
    for x in lst:
        if x in new_lst:
            new_lst=new_lst
        else:
            new_lst+=[x,]
    return new_lst
