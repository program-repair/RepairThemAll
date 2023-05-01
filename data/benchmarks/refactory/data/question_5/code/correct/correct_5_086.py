def top_k(lst, k):
    new_lst = []
    while len(new_lst) != k:
        new_lst.append(max(lst))
        lst.remove(max(lst))
    return new_lst

