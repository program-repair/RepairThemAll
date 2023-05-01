def top_k(lst, k):
    for item in range(len(lst)):
        for test in range(len(lst)):
            if lst[test] < lst[item]:
                lst[test], lst[item] = lst[item], lst[test]
    return lst[:k]
