def sort_age(lst):
    new=[]
    while lst !=[]:
        big=lst[0]
        for i in lst:
            if i[1]>big[1]:
                big=i
        lst.remove(big)
        new.append(big)
    return new
        
            
        
