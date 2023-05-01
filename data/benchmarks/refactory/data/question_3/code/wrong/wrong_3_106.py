def remove_extras(lst):
    # your code here
    result = (lst[0],)
    count = 0
    for item in lst[1:]:
        if item == result[count]:
            count += 1
        else:
            result +=(item,)
            count +=1
    return result
        
        
