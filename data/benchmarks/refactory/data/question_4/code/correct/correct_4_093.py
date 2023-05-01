def sort_age(lst):
    res = []
    a=age_list(lst)
    while lst:
        for i in lst:
            if max(a) == i[1]:
                highest=i
                res= res + [i]
        lst.remove(highest)
        a.remove(highest[1])
    return res


def age_list(lst):
    age_list= []
    for i in range(len(lst)):
        age_list = age_list+ [lst[i][1]]
    return age_list
