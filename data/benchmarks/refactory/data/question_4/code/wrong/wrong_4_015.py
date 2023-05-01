def sort_age(lst):
    sort = []
    while lst: 
        smallest = lst[0]
        for element in lst:
            if element < smallest:
                smallest = element
        a.remove(smallest)
        sort.append(smallest)
    return sort
