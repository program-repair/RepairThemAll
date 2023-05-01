def sort_age(lst):
    newlst = []
    while lst:
        current = lst[0]
        for element in lst:
            if element[1] < current[1]:
                current = element
        newlst += current
        lst.remove(current)
    return newlst
        
