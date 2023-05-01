def top_k(lst, k):
    sorted_lst = lst
    while sorted_lst:
        largest = sorted_lst[0]
        for element in sorted_lst:
            if element > largest:
                largest = element
        sorted_lst.remove(largest)
        sorted_lst.append(largest)
    return sorted_lst[:k-1]
    pass
