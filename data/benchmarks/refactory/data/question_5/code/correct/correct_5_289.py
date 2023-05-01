def top_k(lst, k):
    count = 0
    op = []
    while count < k:
        op += [max(lst)]
        lst.remove(max(lst))
        count += 1
    return op
