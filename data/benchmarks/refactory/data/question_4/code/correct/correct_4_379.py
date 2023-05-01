def sort_age(lst):
    for i in range(len(lst)-1): 
        x = i+1
        for j in range(x,len(lst)):
            if lst[i][1] < lst[j][1]:
                lst[i],lst[j]= lst[j], lst[i]
    return lst
