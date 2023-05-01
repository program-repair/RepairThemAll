def sort_age(lst):
    # Fill in your code here
    sorted_list = []
    
    while a:
        oldest = lst[0]
        
        for element in lst:
            if element[1] > oldest:
                oldest = element[1]
        
        lst.remove(oldest)
        sorted_list.append(oldest)
        
    return sorted_list
