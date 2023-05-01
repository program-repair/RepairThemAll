def sort_age(lst):
    sort = []
    
    while len(lst) > 0:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        
        lst.remove(largest)
        sort.append(largest)

    return sort
