def sort_age(lst):
    """selection sort"""
    l = len(lst)
    for i in range(l):
        largest = lst[i]
        for j in range(i+1,l):
            if lst[j][1] > largest[1]:
                largest = lst[j] #assign new largest value
                lst[i],lst[j] = lst[j],lst[j] #swap positions if larger
    return lst
                
                
