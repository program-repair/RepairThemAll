def top_k(lst, k):
    new_list = []
    while lst:
        maximum = lst[0]
        for i in lst:
            if i > maximum:
                maximum = i
        new_list.append(maximum)
        lst.remove(maximum)
    new_list_2 = []
    counter = 0
    for i in new_list:
        if counter < k:
            new_list_2.append(new_list[counter])
            counter = counter + 1
    return new_list_2
