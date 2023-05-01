def sort_age(lst):
    sorted1 = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element[1] > largest[1]:
                largest = element
        lst.remove(largest)
        sorted1.append(largest)
    return sorted1
        
