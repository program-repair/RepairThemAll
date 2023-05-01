def sort_age(lst):
    
    people = []
    
    while lst:
        
        i = lst[0]
        
        for a in lst:
            
            if a[1] >= i[1] :
                
                i = a
                
        lst.remove(i)
        
        people.append(i)
        
    return final
