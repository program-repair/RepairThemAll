def sort_age(lst):
    ages = []
    output = []
    for item in lst:
        ages.append(item[1])
    for item in lst:
        age = max(ages)
        if age == item[1]:
            output.append(item)
            ages.remove(age)
    return output
