def sort_age(lst):
    lst_len = len(lst) - 1
    while lst_len > 0:
        for i in range(lst_len):
            if lst[i][1] > lst[i+1][1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        lst_len -= 1
    return lst[::-1]
