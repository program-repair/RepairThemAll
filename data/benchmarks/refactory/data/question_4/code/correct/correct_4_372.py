def sort_age(lst):
    sort_lst = []
    while lst:
        high = lst[0]
        for i in lst:
            if i[1] > high[1]:
                high = i
        lst.remove(high)
        sort_lst.append(high)
    return sort_lst
