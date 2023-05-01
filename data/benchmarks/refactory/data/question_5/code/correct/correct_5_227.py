def top_k(lst, k):
    new_lst = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        new_lst.append(largest)
    return new_lst[0:k]
