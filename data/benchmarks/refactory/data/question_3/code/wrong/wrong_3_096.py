def remove_extras(lst):
    result = []
    for i in lst:
        if i not in result:
            result = result + i
    return result
            
            
    # your code here
    pass
