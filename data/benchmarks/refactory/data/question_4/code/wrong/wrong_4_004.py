def sort_age(lst):
    sort = []
    while lst:
        oldest = lst[0]
        for person in lst:
            if person[1] > oldest[1]:
                person = oldest
        a.remove(oldest)
        sort.append(oldest)
        print(lst)
    
            
