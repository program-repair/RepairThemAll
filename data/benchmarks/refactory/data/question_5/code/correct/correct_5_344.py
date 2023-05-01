def top_k(lst, k):
    #assumes not nested lists
    new = []
    count = 0
    while count < k:
        largest = lst[0]
        for ele in lst:
            if ele > largest:
                largest = ele
        lst.remove(largest)
        new.append(largest)
        count = count + 1
    return new
