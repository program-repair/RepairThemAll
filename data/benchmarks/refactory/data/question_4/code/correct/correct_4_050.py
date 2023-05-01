def sort_age(lst):
    for loop in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i][1]<lst[i+1][1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst
