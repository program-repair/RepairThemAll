def sort_age(lst):
    new = []
    while lst:
        smallest = lst[0][1]
        for i in lst:
            if i[1] < smallest:
                smallest = i[1]
        lst.remove(smallest)
        new.append(smallest)
    return new
