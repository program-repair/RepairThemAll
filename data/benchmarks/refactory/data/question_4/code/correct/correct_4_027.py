def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]
        largestx = lst[0][1]
        for element in lst:
            if element[1] > largestx:
                largestx = element[1]
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort
