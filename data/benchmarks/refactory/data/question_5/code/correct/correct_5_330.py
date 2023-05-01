def top_k(lst, k):
    new_list = []
    while k > 0:
        new_list.append(max(lst))
        lst.remove(max(lst))
        k = k-1
    return new_list
