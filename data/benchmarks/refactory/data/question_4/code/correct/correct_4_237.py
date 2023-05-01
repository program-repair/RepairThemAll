def sort_age(lst):
    if lst == []:
        return []
    else:
        max_age = max(lst, key = lambda x: x[1])
        lst.remove(max_age)
        return [max_age] + sort_age(lst)
        
    
            
        
 
