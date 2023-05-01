def sort_age(lst):
    lst1 = []  
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        lst1.append(largest)
    return lst1

            
