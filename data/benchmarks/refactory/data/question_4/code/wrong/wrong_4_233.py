def sort_age(lst):
    sort = []
    while lst: # a is not []
        smallest = (lst[0])[1]
        for element in lst:
            if element[1] < smallest:
                smallest = element
        lst.remove(smallest)
        sort.append(smallest)
    return lst

