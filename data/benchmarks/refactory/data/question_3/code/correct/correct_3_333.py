def remove_extras(lst):
    index = 0
    listNumber = []
    result = []
    for i in lst:
        listNumber.append(i)
        count = 0
        for j in listNumber:
            if i == j:
                count += 1
        if count <= 1:
            result.append(i)
        index += 1
    return result
