def top_k(lst, k):
    stop = False
    result = []
    while k>0:
        highest = 0
        index = 0
        for i in range(0,len(lst)):
            if lst[i]>highest:
                index = i
                highest = lst[i]
        result = result + [highest]
        lst.pop(index)
        k = k - 1
    return result
