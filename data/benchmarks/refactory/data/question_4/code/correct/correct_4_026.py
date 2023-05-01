def sort_age(lst):
    sort = []
    while lst:
        oldest = lst[0]
        for person in lst:
            if person[1] >= oldest[1]:
                oldest = person
        lst.remove(oldest)
        sort.append(oldest)
    return sort
    
            
