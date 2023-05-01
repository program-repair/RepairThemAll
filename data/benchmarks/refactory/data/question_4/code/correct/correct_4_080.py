def sort_age(lst):
    new_lst = []
    age = []
    for i in lst:
        age = age + [i[1],]
    while len(lst) != 0:
        for j in lst:
            if j[1] == max(age):
                lst.remove(j)
                age.remove(max(age))
                new_lst = new_lst + [j,]
            
    return new_lst
        
