def sort_age(lst):
    new =[]
    while lst:
        index = 0
        oldest = lst[0][1]
        for i in range(1, len(lst)):
            if lst[i][1] >oldest:
                oldest = lst[i][1]
                index = i
        new.append(lst[index])
        del lst[index]
    return new
        
        
        
