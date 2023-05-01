def remove_extras(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] not in result:
            result += [lst[i],]
            continue
    return result
