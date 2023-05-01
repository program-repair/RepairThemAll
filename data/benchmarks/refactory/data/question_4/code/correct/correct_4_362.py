def sort_age(lst):
    ages = []
    output = []
    for item in lst:
        ages.append(item[1])
    while ages:
        age = max(ages)
        for item in lst:
            if age == item[1]:
                output.append(item)
                ages.remove(age)
    return output
