def sort_age(lst):
    list1 = []
    while lst:
        biggest = lst[0][1]
        b = lst[0]
        for i in range(1,len(lst)):
            if lst[i][1] > biggest:
                biggest = lst[i][1]
                b = (lst[i],)
        lst.remove(b)
        list1.append(b)
    return list1

