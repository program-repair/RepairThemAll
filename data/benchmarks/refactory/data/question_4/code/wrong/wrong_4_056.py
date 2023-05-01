def sort_age(lst):
    # Fill in your code here
    new_lst = []
    while lst:
        for i in range(len(lst)):
            oldest = lst[0]
            if lst[i][1] > oldest[1]:
                oldest = lst[i] 
        lst.remove(oldest)
        new_lst.append(oldest)
        
    return new_lst
            
        
