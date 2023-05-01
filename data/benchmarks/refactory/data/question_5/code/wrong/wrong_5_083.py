def top_k(lst, k):
    result = []
    for i in range(len(lst)):
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        result.append(largest)
    return lst[:k]
