def top_k(lst, k):
    for start in range (len(lst) - 1):
        for i in range(start, len(lst)):
            if lst[i] > lst[start]:
                lst[i], lst[start] = lst[start], lst[i]
    return lst[:k]
