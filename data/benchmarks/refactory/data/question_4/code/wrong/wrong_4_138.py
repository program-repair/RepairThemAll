def sort_age(lst):
    while lst: # a is not []
        smallest = lst[0]
        for element in lst:
            if element[1] < smallest[1]:
                smallest = element
        lst.remove(smallest)
        sort.append(smallest)
