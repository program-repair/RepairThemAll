def sort_age(lst):
    for x in range(len(lst)):
        max = x
        for i in range(x, len(lst)):
            if lst[i][1] > lst[max][1]:
                max = i
        lst[max], lst[x] = lst[x], lst[max]
    return lst
