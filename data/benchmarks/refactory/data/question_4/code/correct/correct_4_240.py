def sort_age(lst):
    a = lst
    for i in range(len(lst)):        
        for i in range(len(a)-1):
            if a[i][1] < a[i+1][1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a
