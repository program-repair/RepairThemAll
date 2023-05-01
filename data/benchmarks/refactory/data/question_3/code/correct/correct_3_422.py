def remove_extras(lst):
    result=[]
    for i in lst:
        if i in result:
            continue
        else:
            result+=[i,]
    return result
    pass
