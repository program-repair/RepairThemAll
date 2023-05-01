def remove_extras(lst):
    product = []
    for element in lst:
        if element in product:
            continue
        else:
            product = product + [element]
    return product
