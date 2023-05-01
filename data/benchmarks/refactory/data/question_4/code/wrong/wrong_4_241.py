def sort_age(lst):
    list1 = ()
    i = 0
    smallest = lst[0][1]
    s = lst[0]
    for i in range(1,len(lst)):
        if lst[i][1] < smallest:
            smallest = lst[i][1]
            s = lst[i]
    list1 += s
    return list1
