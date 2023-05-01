def sort_age(lst):
    result = []
    while lst != []:
        largest_tup = lst[0]
        largest = lst[0][1]
        for i in lst:
            if i[1] > largest:
                largest_tup = i 
                largest = i[1]
        lst.remove(largest_tup)
        result.append(largest_tup)
    return result
    
