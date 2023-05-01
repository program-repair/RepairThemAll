def remove_extras(lst):
    length = len(lst)
    if length == 0:
        return []
    result = [lst[0]]
    for i in range(1,length):
        if lst[i] not in result:
            result = result + [lst[i]]
    return result
