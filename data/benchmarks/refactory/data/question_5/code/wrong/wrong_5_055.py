def top_k(lst, k):
    values = []
    greatest = lst[0]
    while len(values) < k:
        for item in lst:
            if item > greatest:
                greatest = item
        lst.remove(greatest)
        values.append(greatest)
        greatest = lst[0]
    return values
