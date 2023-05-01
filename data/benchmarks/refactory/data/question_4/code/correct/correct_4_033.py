def sort_age(lst):
    tmp = []
    ages = [x[1] for x in lst]
    while len(ages) > 0:
        age = max(ages)
        for x in lst:
            if x[1] == age:
                tmp.append(x)
                ages.remove(age)
                continue
    return tmp
