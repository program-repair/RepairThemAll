def sort_age(lst):
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[j][1] > lst[i][1]:
                x = lst[i]
                lst[i] = lst[j]
                lst[j] = x
    return lst
