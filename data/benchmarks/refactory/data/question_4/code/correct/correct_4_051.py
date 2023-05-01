def sort_age(lst):
    def for_age(lst):
        for i in range(len(lst)):
            if i == 0: continue
            else:
                while i > 0:
                    if lst[i][1] < lst[i-1][1]:
                        lst[i], lst[i-1] = lst[i-1], lst[i]
                        i -= 1
                    else: i = 0
    for_age(lst)
    lst.reverse()
    return lst
