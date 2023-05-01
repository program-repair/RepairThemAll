def top_k(lst, k):
    ret = []
    for i in range(k):
        max_int_pos = lst.index(max(lst))
        ret.append(lst.pop(max_int_pos))
    return ret
