def sort_age(lst):
    a = lst
    sort = []
    while a:
        largest = a[0][1]
        for item in a:
            if item[1] >largest:
                largest = item
        a.remove(largest)
        sort.append(largest)
        print(sort)# Fill in your code here
    
