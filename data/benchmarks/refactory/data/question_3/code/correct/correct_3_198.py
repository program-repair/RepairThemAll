def remove_extras(lst):
    result=[]
    for i in lst:
        if i in result:
            continue
        result+= [i]
    return result
