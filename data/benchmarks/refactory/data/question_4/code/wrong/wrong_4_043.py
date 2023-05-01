def sort_age(lst):
    result = [lst[0]]
    for i in lst[1:]:
        if i[1] > result[0][1]:
            result.insert(0, i)
        elif i[1] < result[-1][1]:
            result.append(i)
        else:
            for j in range(len(result) - 1):
                if i[1] < result[j][1] and i[1] > result[j+1][1]:
                    result.insert(j, i)
    return result
