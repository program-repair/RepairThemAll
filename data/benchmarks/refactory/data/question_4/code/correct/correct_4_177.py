def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element[1] > largest[1]:
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort
