def top_k(lst, k):
    # Fill in your code here
    sort = []
    while lst: # a is not []
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort[:k]
