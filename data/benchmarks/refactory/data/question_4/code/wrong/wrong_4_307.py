def sort_age(lst):
    sort =[]
    while lst:
        smallest = lst[0]
        for i in lst:
            if i< smallest:
                smallest = i
        lst.remove(smallest)
        sort.append(smallest)
    return sort
    pass
