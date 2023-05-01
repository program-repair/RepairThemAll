def sort_age(lst):
    # Fill in your code here
    sorted_list = []
    
    while lst:
        oldest = lst[0]
        
        for element in lst:
            if element[1] > oldest[1]:
                oldest = element
        
        lst.remove(oldest)
        sorted_list.append(oldest)
        
    return sorted_list
