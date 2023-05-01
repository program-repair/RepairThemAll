def sort_age(lst):
    for i in range(len(lst)-1):
        for a in range(i+1, len(lst)):
            if lst[i][1] < lst[a][1]:
                lst[i]= lst[a]
                lst[a]= lst[i]
    return lst

        
