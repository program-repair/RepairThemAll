def sort_age(lst):
    holder=[]
    for x in lst:
        if holder==[]:
            holder=x
        elif x[1]>holder[1]:
            holder=x
    return holder+sort_age(lst[1:])
        
                
            
        
