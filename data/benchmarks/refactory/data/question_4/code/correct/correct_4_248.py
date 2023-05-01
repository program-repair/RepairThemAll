def sort_age(lst):
    newlst = []
    while lst:
        largest = lst[0]
        for el in lst:
            if el[1] > largest[1]:
                largest = el
        newlst.append(largest)
        lst.remove(largest) #when it repeats, largest will take on the new first element in lst
    return newlst
        
