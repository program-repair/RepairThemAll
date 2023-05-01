def sort_age(lst):
    arranged = []
    while lst:
        oldest = lst[0]
        for person in lst:
            if person > oldest:
                oldest = person
        lst.remove(oldest)
        arranged.append(oldest)
    return arranged
    pass
