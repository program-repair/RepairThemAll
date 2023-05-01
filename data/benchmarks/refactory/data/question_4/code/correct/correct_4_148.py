def sort_age(lst):
    sort = []
    while lst:
        oldest = lst[0]
        for x in lst:
            if x[1] > oldest[1]:
                oldest = x
        lst.remove(oldest)
        sort.append(oldest)
    return sort
            
        
