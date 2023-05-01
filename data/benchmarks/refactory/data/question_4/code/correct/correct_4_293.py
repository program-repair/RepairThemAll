def sort_age(lst):
    sorted = []
    while lst:
        oldest = lst[0]
        for element in lst:
            if element[1] > oldest[1]:
                oldest = element
        lst.remove(oldest)
        sorted.append(oldest)
    return sorted
            
