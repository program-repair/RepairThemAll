def top_k(lst, k):
    result = [lst[0]]
    for i in lst[1:]:
        if i > result[0]:
            result.insert(0, i)
        elif i <= result[-1]:
            result.append(i)
        else:
            for j in range(1, len(result) - 1):
                if i <= result[j] and i >= result[j+1]:
                    result.insert(j+1, i)
                    break
    return result[:k]
