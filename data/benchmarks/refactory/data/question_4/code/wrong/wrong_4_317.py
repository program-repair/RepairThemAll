def sort_age(lst):
    a = []
    for i in lst:
        a.append(i[1])
    print(a)
    sort = []
    while a:
        smallest = a[0]
        for element in a:
            if element < smallest:
                smallest = element
        a.remove(smallest)
        sort.append(smallest)
    print(sort)
    lst2 = []
    counter = 0
    for i in sort:
        for j in lst:
            if j[1] == i:
                lst2.append(j)
                counter += 1
    return lst2
