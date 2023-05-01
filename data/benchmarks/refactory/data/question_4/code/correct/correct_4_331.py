def sort_age(lst):
    for i in range(len(lst)-1,0,-1):
        for a in range(i):
            if lst[a][1]<lst[a+1][1]:
                temp = lst[a]
                lst[a] = lst[a+1]
                lst[a+1] = temp
    return lst
