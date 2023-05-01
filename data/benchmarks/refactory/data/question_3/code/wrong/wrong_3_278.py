def remove_extras(lst):
    if lst == []:
        return None
    else: 
        result = [lst[0],]
        for e in lst:
            if e not in result:
                result.append(e)
            else:
                continue
        return result
