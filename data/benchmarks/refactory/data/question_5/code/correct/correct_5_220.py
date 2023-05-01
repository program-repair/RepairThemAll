def top_k(lst, k):
    new_lst = []

    while lst:
        big = lst[0]
        for i in lst:
            if i > big:
                big = i
        lst.remove(big)
        new_lst.append(big)

    return new_lst[:k]
