def sort_age(lst):
    compiled = []
    result = []
    for i in lst:
        compiled = compiled + [i[1]]
    compiled.sort()
    compiled.reverse()
    for i in compiled:
        for j in lst:
            if i == j[1]:
                result = result + [j]
    return result
