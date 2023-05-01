def top_k(lst, k):
    product = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i>largest:
                largest = i
        lst.remove(largest)
        product.append(largest)
    return product[:k]
