def sort_age(lst):
    # Fill in your code here
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i][1] < lst[j][1]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
