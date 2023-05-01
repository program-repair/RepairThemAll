def top_k(lst, k):
    new_lst = []
    while lst:
        largest = lst[0]
        for numbers in lst:
            if numbers > largest:
                largest = numbers
        new_lst.append(largest)
        lst.remove(largest)
    return new_lst[:k]
