def sort_age(lst):
    for i in range(len(lst)):
        position = i
        biggest = position
        for a in range(position, len(lst)):
            if lst[a][1] > lst[biggest][1]:
                biggest = a
        tmp = lst[position]
        lst[position] = lst[biggest]
        lst[biggest] = tmp
    return lst
