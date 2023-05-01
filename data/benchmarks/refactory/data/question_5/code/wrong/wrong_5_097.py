def top_k(lst, k):
    # Fill in your code here
    sort = []
    while lst:
        largest = lst[0]
        for i in range(len(lst)):
            if lst[i] > largest:
                largest = lst[i]
        sort.append(largest)
        lst.remove(largest)
    return sort[:k + 1]
        
