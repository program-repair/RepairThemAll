def sort_age(lst):
    
    sort = []
    
    while lst:

        largest = lst[0]

        for x in lst:

            if x[1] > largest[1]:

                largest = x

        lst.remove(largest)

        sort.append(largest)

    return sort
