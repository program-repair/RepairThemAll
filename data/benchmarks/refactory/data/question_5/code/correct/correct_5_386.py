def top_k(lst, k):
    num, result = max(lst), []
    while len(result) < k:
        if num in lst:
            result.append(num)
            lst.remove(num)
        elif num not in lst:
            num -= 1
            continue
    return result
