def sort_age(lst):
    new_lst = []
    while lst:
        oldest = lst[0]
        for i in range(len(lst)):
            if lst[i][1] > oldest[1]:
                oldest = lst[i]
        lst.remove(oldest)
        new_lst.append(oldest)
    print(new_lst)
