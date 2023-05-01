def sort_age(lst):
    list1 = []
    smallest = lst[0][1]
    s = (lst[0],)
    for j in range(1,len(lst)):
        
        for i in range(1,len(lst)-1):
            if lst[i][1] < smallest:
                smallest = lst[i][1]
                s = (lst[i],)
        list1 += s
    return list1
