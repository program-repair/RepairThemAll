def sort_age(lst):
    if len(lst)<=1:
        return lst
    else:
        used_lst=lst.copy()
        ages=()
        for i in lst:
            ages+=(i[1],)
        for i in lst:
            if i[1]==max(ages):
                new_lst=[i]
                used_lst.remove(i)
        return new_lst+sort_age(used_lst)
