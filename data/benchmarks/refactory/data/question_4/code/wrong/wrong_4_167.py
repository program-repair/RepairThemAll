def sort_age(lst):
    sortt = [] #empty list
    while lst:
        largest = lst[0] #let the first element be the largest first
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        sortt.append(largest)
    return sort
