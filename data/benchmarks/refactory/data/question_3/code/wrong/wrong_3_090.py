def remove_extras(lst):
    result=[]
    for i in lst:
        if i in lst[:i]:
            continue
        result+= [i]
    return result
