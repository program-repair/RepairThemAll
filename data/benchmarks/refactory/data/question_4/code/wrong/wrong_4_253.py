def sort_age(lst):
    list1 = []
    while lst:
        biggest = lst[0]
       
        for i in lst:
            if i[1] > biggest[1]:
                biggest = i[1]
                
        lst.remove(biggest)
        list1.append(biggest)
    return list1

