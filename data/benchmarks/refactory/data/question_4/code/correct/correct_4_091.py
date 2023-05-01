def sort_age(lst):
    sorted_lst = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] < smallest[1]:
                smallest = i
        lst.remove(smallest)
        sorted_lst.append(smallest)
    sorted_lst.reverse()
    return sorted_lst
