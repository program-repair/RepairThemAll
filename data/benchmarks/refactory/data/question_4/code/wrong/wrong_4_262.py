def sort_age(lst):
    s = []
    while lst:
        smallest = lst[0]
        for element in lst:
            if element[1]<smallest[1]:
                smallest = element
        lst.remove(smallest)
        s.append(smallest)
        s.reverse()
    return s
