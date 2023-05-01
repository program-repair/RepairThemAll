def sort_age(lst):
    for i in range(len(lst)-1):
        if lst[i+1][1] < lst[i][1]:
            x = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = x
    return lst
