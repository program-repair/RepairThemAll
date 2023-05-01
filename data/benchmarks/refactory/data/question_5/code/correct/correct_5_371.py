def top_k(lst, k):
    lst2 = []
    largest = lst[0]
    while lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        lst2.append(largest)
    return lst2[0:k]
