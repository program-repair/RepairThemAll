def top_k(lst, k):
    product = []
    while k > 0:
        product += [max(lst)]
        k = k -1
        lst.remove(max(lst))
    return product
