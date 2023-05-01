def sort_age(lst):
    for start in range(len(lst)):
        minimum = start
        for i in range(start,len(lst)):    
            if lst[i][1] < lst[minimum][1]:
                minimum = i
        lst[start], lst[minimum] = lst[minimum], lst[start]
    lst.reverse()            
    return lst
        
