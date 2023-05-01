def remove_extras(lst):
    for i in lst:
        result=lst.count(i)
        while result>1:
            lst.remove(i)
            result=result-1
    return lst 
            
    
 
