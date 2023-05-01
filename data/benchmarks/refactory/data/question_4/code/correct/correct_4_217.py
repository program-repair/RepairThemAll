def sort_age(lst):
    a = []
    for i in lst:
        a.append(i[1])
    sort = []
    while a:
        largest = a[0]
        for element in a:
            if element > largest:
                largest = element
        a.remove(largest)
        sort.append(largest)
    lst2 = []
    counter = 0
    for i in sort:
        for j in lst:
            if j[1] == i:
                lst2.append(j)
                counter += 1
    return lst2
