def top_k(lst, k):
    new = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        new.append(largest)
        lst.remove(largest)
    if k > len(new):
        return new
    else:
        return new[:k]
