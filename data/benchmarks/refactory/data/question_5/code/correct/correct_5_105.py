def top_k(lst, k):
    sotsot = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sotsot.append(largest)
    return sotsot[:k]
