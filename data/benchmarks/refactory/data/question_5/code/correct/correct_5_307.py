def top_k(lst, k):
    n = len(lst) - 1
    while n > 0:
        for i in range(n):
            if lst[i]> lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n = n-1
    lst.reverse()
    return lst[:k]
