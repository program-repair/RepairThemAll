def sort_age(lst):
    new = []
    while lst:
        largest = lst[0][1]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
        for j in lst:
            if largest in j:
                lst.remove(j)
                new.append(j)
    return new

