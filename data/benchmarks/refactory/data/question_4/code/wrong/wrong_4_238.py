def sort_age(lst):
    sort = []
    while lst:
        oldest = list[0]
        for x in lst:
            if x[1] > oldest[1]:
                oldest = x
        a.remove(oldest)
        sort.append(oldest)
    return sort
            
        
