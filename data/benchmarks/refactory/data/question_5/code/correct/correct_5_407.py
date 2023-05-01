def top_k(lst, k):
    new = []
    ans = []
    for i in lst:
        index = 0
        for x in new:
            if i < x:
                index += 1
        new.insert(index, i)
    for i in range(k):
        ans.append(new[i])
    return ans
