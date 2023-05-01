def sort_age(lst):
    arranged = []
    while lst:
        oldest = lst[0]
        for person in lst:
            if person[1] > oldest[1]:
                oldest = person
        lst.remove(oldest)
        arranged.append(oldest)
    return arranged
    pass
