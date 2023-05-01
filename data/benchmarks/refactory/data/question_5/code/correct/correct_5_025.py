def top_k(lst, k):
    new_lst = []
    while len(new_lst) < k:
        maximum = max(lst)
        new_lst.append(maximum)
        lst.remove(maximum)

    return new_lst
