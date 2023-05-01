def sort_age(lst):
    all_age = []
    for person in lst:
        all_age += [person[1],]
    result = []
    while len(result) < len(lst):
        for person in lst:
            if person[1] == max(all_age):
                result += (person,)
        all_age.remove(max(all_age))
    return result
