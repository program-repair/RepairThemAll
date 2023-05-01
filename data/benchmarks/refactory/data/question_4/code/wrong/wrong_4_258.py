def sort_age(lst):
    res = []
    age_list= []
    while lst:
        for i in range(len(lst)):
            age_list = age_list+ [lst[i][1]]
        for i in lst:
            if max(age_list) == i[1]:
                res= res + [i]
            else:
                res = res
        lst.remove(i)
        age_list.remove(i[1])
    return res 
