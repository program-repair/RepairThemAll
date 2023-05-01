def sort_age(lst):
    largest = lst[0][1]
    sort1 = []
    for i in lst:
        if i > largest:
            largest = i
            sort1.append(i)
    return sort1
            
            
