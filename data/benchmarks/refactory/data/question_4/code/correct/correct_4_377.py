def sort_age(lst):
    lst2 = []
    lst_num = []
    for x in range(len(lst)):
        lst_num.append(lst[x][1])
    
    lst_num_sorted = []
    while lst_num:
        lst_num_sorted.append(max(lst_num))
        lst_num.remove(max(lst_num))
        
    for y in lst_num_sorted:
        for z in lst:
            if y == z[1]:
                lst2.append(z)
    return lst2
