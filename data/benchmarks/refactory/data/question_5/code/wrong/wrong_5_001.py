def top_k(lst, k):
    result = []
    while k >= 0:
        big = max(lst)
        result.append(big)
        lst.remove(big)
        k -= 1
    return result
