def sort_age(lst):
    sort = []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort
