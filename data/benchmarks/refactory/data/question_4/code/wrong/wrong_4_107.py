def sort_age(lst):
    smallest =  lst[0][1]
    sort = []
    while lst:
        for k in lst:
            if k[1] < smallest:
                smallest = k[1]
                smallest_tuple = k
        lst.remove(k)
        sort.append(k)
                
