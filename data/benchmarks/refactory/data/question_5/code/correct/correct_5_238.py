def top_k(lst, k):
    lst = sorting(lst)
    new = []
    for i in range(k):
        new.append(lst[0])
        del lst[0]
    return new

def sorting(lst):
    sorted_lst = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i < smallest:
                smallest = i
        lst.remove(smallest)
        sorted_lst.append(smallest)
    sorted_lst.reverse()
    return sorted_lst
