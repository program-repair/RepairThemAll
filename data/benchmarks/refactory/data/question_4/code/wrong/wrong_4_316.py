def sort_age(lst):
    lst1 = []
    
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
    lst.remove(largest)
    lst1.append(largest)
    return lst1

            
