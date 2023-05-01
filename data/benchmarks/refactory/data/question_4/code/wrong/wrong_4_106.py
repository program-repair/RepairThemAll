def sort_age(lst):
    smallest =  lst[0][1]
    sort = []
    while lst:
        for k in lst:
            if k[1] < smallest:
                smallest = k[1]
        a.remove(smallest)
        sort.append(smallest)
                
