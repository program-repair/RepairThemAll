def sort_age(lst):
    sort=[]
    while lst:
        oldest=lst[0]
        for element in lst:
            if element[1]>oldest[1]:
                oldest=element
        lst.remove(oldest)
        sort.append(oldest)
    return sort 
        
