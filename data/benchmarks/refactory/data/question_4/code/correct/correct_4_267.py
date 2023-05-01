def sort_age(lst):
    sort = []

    while lst:
        largest_element = lst[0]
        largest_value = lst[0][1]
        for element in lst:
            if element[1] > largest_value:
                largest_element = element
                largest_value = element[1]
            else:
                continue
        lst.remove(largest_element)
        sort.append(largest_element)
    return sort
