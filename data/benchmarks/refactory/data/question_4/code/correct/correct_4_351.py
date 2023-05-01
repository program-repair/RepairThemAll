def sort_age(lst):
    for start in range (len(lst) - 1):
        for i in range(start, len(lst)):
            if lst[i][1] > lst[start][1]:
                lst[i], lst[start] = lst[start], lst[i]
    return lst
