def sort_age(lst):
    while lst:
        smallest = lst[0]
    for e in lst[1:]:
        if e[1]<smallest:
            smallest = e[1]
    lst.remove(smallest)
    lst.append(smallest)
    return lst
