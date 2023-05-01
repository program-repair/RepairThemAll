def sort_age(lst):
    sort_list = []
    while lst: # a is not []
        smallest = lst[0]
        for element in lst:
            if element[1] < smallest[1]:
                smallest = element
        lst.remove(smallest)
        sort_list.append(smallest)
    return sort_list
