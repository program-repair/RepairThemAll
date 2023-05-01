def top_k(lst, k):
    new = []
    while lst:
        largest = lst[0]
        for a in lst:
            if a > largest:
                largest = a
        lst.remove(largest)
        new.append(largest)
    return new[0:k]
