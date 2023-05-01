def top_k(lst, k):
    new_list = []
    while len(new_list) < k:
        maximum = max(lst)
        new_lst.append(lst)
        lst.remove(maximum)

    return new_lst
