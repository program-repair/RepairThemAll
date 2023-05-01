def top_k(lst, k):
    sorted_lst = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sorted_lst.append(largest)
    return sorted_lst[:k]
    pass
