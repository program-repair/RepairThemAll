def sort_age(lst):
    sort = []
    while lst:
        smallest = lst[0]
        for element in a:
            if element[1] < smallest[1]:
                smallest = element
            lst.remove(smallest)
            sort.append(smallest)
        
    pass
