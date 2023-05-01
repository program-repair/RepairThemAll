def top_k(lst, k):
    sort = []
    while lst:
        big = max(lst)
        sort.append(big)
        lst.remove(big)
    output = []
    for i in range(k):
        output.append(sort[i])
    return output
