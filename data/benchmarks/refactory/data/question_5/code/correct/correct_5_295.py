def top_k(lst, k):
    unsorted = lst
    result = []
    while True:
        if len(result) == k:
            break
        result += [max(unsorted),]
        unsorted.remove(max(unsorted))
    return result
