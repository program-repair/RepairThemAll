def sort_age(lst):
    new = []
    for x in lst:
        index = 0
        for i in new:
            if x[1] < i[1]:
                index += 1
        new.insert(index,x)
    return new
