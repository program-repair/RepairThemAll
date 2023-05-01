def sort_age(lst):
    new = []
    while lst:
        largest = lst[0][1]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
        lst.remove(i)
        new.append(i)
    return new
