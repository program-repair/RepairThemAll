def sort_age(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i][1]> lst[i+1][1]:
            new_lst.append(lst[i])
    return lst        
            
        
    pass
