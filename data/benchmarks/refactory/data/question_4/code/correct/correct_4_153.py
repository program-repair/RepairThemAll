def sort_age(lst):
    sort1 = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        sort1.append(largest)
    return sort1



            
            
