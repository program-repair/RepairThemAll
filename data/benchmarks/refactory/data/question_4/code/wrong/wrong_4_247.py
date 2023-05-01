def sort_age(lst):
    list1 = []
    while lst:
        biggest = lst[0][1]
        b = lst[0]
        for i in range(1,len(lst)-1):
            if lst[i][1] > biggest:
                biggest = lst[i][1]
                s = (lst[i],)
        lst.remove(biggest)
        list1.append(biggest)
    return list1

