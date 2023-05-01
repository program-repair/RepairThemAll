def sort_age(lst):
    sort = []
    while lst:
        smallest = lst[0]
        print(type(smallest))
        for element in lst:
            print(type(element[1]))
            if element[1] > smallest[1]:
                smallest = element
        lst.remove(smallest)
        sort.append(smallest)
    return sort
