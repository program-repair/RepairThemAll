def remove_extras(lst):
    s = []
    for n in lst: 
        if n not in s:  
           s.append(n)
    return s 
    
