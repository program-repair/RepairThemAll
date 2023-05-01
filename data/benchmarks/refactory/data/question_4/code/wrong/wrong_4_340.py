def sort_age(lst):
    l = len(lst)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (lst[j][1] > lst[j + 1][1]):
                temp = lst[j]
                lst[j]= lst[j + 1]
                lst[j + 1]= temp
    return lst
