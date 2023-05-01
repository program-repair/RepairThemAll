def sort_age(lst):
    result = []
    maximum = 0
    for i in lst:
        if i[1] > maximum:
            maximum = i[1]
            result.insert(0,i)
        else:
            result.append(i)
    return result
