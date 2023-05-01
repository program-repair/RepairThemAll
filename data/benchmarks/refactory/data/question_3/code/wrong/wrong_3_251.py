def remove_extras(lst):
    
    result = lst
    for i in result:
        
        if lst.count(i) > 1:
            result.remove(i)
            continue
            

        
    return result
    pass
