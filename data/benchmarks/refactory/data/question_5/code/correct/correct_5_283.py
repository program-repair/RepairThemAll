def top_k(lst,k):
    n = len(lst)
    result = []
    while n !=0:
        test =[]
        for counter in range(n):
            test.append(lst[counter])
        first = max(test)
        for counter in range(n):
            if lst[counter] == first:
                result.append(lst.pop(counter))
                break
        n = len(lst)
    return result[:k]
