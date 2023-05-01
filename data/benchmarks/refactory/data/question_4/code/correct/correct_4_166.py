def sort_age(lst):
    if lst == []:
        return lst
    else:
        age_lst, new_lst = [], []
        for x in lst:
            age_lst.append(x[1])
        while age_lst:
            max_age = max(age_lst)
            for i in lst:
                if i[1] == max_age:
                    new_lst.append(i)
                    age_lst.remove(i[1])
        return new_lst
    pass
