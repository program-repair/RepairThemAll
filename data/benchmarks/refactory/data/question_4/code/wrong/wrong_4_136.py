def sort_age(lst):
    a = lst
    sort = []
    smallest = a[0][1]
    while   a: # a is not []
        for element in  a:
            if element[1] > smallest:
                smallest = element
        a.remove(smallest)
        sort.append(smallest)

        
    pass
