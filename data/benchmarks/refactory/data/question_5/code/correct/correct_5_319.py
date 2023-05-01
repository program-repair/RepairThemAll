def top_k(lst, k):
    res =[]
    while lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest =element
        lst.remove(largest)
        res.append(largest)
    return res[:k]
