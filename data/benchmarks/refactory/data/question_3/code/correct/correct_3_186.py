def remove_extras(lst):
    # your code here
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
