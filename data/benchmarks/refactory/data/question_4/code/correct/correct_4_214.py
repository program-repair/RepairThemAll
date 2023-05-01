def sort_age(lst):
    new = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        new.append(largest)
    return new
