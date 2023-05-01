def sort_age(lst):
    new = []
    while lst:
        largest = lst[0]
        for ele in lst:
            if ele[1] > largest:
                largest = ele
        a.remove(largest)
        new.append(largest)
    return new
        
