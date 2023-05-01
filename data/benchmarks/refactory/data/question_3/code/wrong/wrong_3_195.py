def remove_extras(lst):
    n = len(lst)
    for counter1 in range(n):
        for counter2 in range(n):
            if lst[counter1] == lst[counter2]:
                lst = lst[:counter1] + lst[counter1 + 1:]
    return lst
