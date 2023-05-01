def top_k(lst, k):
    new_lst = []
    for i in range(k):
        new_lst.append(lst.remove(max(lst)))
    return new_lst
    pass
