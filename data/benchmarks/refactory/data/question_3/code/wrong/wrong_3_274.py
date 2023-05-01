def remove_extras(lst):
    result = lst[0]
    for e in lst:
        if e not in result:
            result.add(e)
        else:
            continue
    return result
