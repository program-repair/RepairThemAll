def sort_age(lst):
    sort = []
    while lst:
        largest = a[0] 
        for element in a: 
            if element > smallest: 
                largest = element 
        lst.remove(largest)
        sort.append(largest) 
    print(lst)
