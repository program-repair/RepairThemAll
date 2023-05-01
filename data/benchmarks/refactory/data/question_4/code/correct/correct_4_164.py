def sort_age(lst):
    n = len(lst)-1
    for i in range(0,n):
        for j in range(i+1,len(lst)):
            if lst[i][1]<lst[j][1]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst
