def top_k(lst, k):
    result = []
    while len(result) < k:
        result.append(lst.pop(lst.index(max(lst))))
    return result
