def remove_extras(lst):
    result = []
    check = set()
    for element in lst:
        if element not in check:
            result.append(element)
            check.add(element)
    return result
