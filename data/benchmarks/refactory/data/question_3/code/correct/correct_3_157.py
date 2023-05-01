def remove_extras(lst):
    result = []

    for element in lst:
        if element not in result:
            result.append(element)
    return result
        
