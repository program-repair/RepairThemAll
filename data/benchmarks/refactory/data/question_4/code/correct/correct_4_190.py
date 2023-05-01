def sort_age(lst):
    a = lst
    sort = []
    while   a: # a is not []
        smallest = a[0][1]
        b=a[0]
        for element in  a:
            if element[1] > smallest:
                smallest = element[1]
                b=element
        a.remove(b)
        sort.append(b)
    return sort
