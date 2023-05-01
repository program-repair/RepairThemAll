def top_k(lst, k):
    for x in range(k+1):
        max = x
        for i in range(x, len(lst)):
            if lst[i] > lst[max]:
                max = i
        if x <= (len(lst) - 1):
            lst[max], lst[x] = lst[x], lst[max]
    new = lst[:k]
    return new
