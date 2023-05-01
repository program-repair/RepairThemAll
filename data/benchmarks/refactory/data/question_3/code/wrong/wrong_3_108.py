def remove_extras(lst):
    # your code here
    result = (lst[0],)
    for item in lst[1:]:
        if item in result:
            continue
        else:
            result +=(item,)
    return list(result)
        
        
