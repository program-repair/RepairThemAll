def sort_age(lst):
    """selection sort: O(n^2) time"""
    l = len(lst)
    for i in range(l):
        largest = lst[i]
        for j in range(i+1,l):
            if lst[j][1] > largest[1]:
                largest = lst[j] #assign new largest value
                lst[i],lst[j] = lst[j],lst[i] #swap positions if larger
        #print(i,lst)
    return lst
