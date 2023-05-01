def remove_extras(lst):
    result = []
    for item in lst:
        if item not in result:
            result += item
    return result
