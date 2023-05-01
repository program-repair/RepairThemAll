def remove_extras(lst):
    result = []
    for elem in lst:
        if elem not in result:
            result.append(elem)
    return result
