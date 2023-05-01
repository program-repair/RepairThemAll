def sort_age(lst):
    
    people = []
    
    while lst:
        
        i = lst[0]
        
        for a in lst:
            
            if i[1] <= a[1] :
                
                i = a
                
        lst.remove(i)
        final.append(i)
        
    return final
