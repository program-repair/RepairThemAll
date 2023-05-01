def sort_age(lst):
    largest = lst[0][1]
    sort1 = []
    for i in lst:
        if i[1] > largest:
            largest = i[1]
        sort1.append(i)
    return sort1
            
            
